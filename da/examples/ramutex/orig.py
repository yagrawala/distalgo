# -*- generated by 1.0.9 -*-
import da
PatternExpr_260 = da.pat.TuplePattern([da.pat.ConstantPattern('Done'), da.pat.BoundPattern('_BoundPattern263_')])
PatternExpr_282 = da.pat.TuplePattern([da.pat.ConstantPattern('Request'), da.pat.FreePattern('timestamp')])
PatternExpr_289 = da.pat.FreePattern('source')
PatternExpr_317 = da.pat.TuplePattern([da.pat.ConstantPattern('Reply'), da.pat.FreePattern('c1')])
PatternExpr_324 = da.pat.FreePattern('source')
PatternExpr_266 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.FreePattern(None)]), da.pat.TuplePattern([da.pat.ConstantPattern('Done'), da.pat.BoundPattern('_BoundPattern276_')])])
_config_object = {}
import sys

class P(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._PReceivedEvent_0 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_0', PatternExpr_260, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_1', PatternExpr_282, sources=[PatternExpr_289], destinations=None, timestamps=None, record_history=None, handlers=[self._P_handler_281]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_2', PatternExpr_317, sources=[PatternExpr_324], destinations=None, timestamps=None, record_history=None, handlers=[self._P_handler_316])])

    def setup(self, ps, nrounds, **rest_402):
        super().setup(ps=ps, nrounds=nrounds, **rest_402)
        self._state.ps = ps
        self._state.nrounds = nrounds
        self._state.reqc = None
        self._state.waiting = set()
        self._state.replied = set()

    def run(self):

        def anounce():
            self.output('In cs!')
        for i in range(self._state.nrounds):
            self.cs(anounce)
        self.send(('Done', self._id), to=self._state.ps)
        super()._label('_st_label_251', block=False)
        p = None

        def UniversalOpExpr_252():
            nonlocal p
            for p in self._state.ps:
                if (not PatternExpr_266.match_iter(self._PReceivedEvent_0, _BoundPattern276_=p, SELF_ID=self._id)):
                    return False
            return True
        _st_label_251 = 0
        while (_st_label_251 == 0):
            _st_label_251 += 1
            if UniversalOpExpr_252():
                _st_label_251 += 1
            else:
                super()._label('_st_label_251', block=True)
                _st_label_251 -= 1
        self.output('Terminating..')

    def cs(self, task):
        super()._label('start', block=False)
        self._state.reqc = self.logical_clock()
        self.send(('Request', self._state.reqc), to=self._state.ps)
        super()._label('_st_label_200', block=False)
        _st_label_200 = 0
        while (_st_label_200 == 0):
            _st_label_200 += 1
            if (len(self._state.replied) == len(self._state.ps)):
                _st_label_200 += 1
            else:
                super()._label('_st_label_200', block=True)
                _st_label_200 -= 1
        task()
        super()._label('release', block=False)
        self._state.reqc = None
        self.send(('Reply', self.logical_clock()), to=self._state.waiting)
        super()._label('end', block=False)
        self._state.waiting = set()
        self._state.replied = set()

    def _P_handler_281(self, timestamp, source):
        if ((self._state.reqc == None) or ((timestamp, source) < (self._state.reqc, self._id))):
            self.send(('Reply', self.logical_clock()), to=source)
        else:
            self._state.waiting.add(source)
    _P_handler_281._labels = None
    _P_handler_281._notlabels = None

    def _P_handler_316(self, c1, source):
        if ((not (self._state.reqc is None)) and (c1 > self._state.reqc)):
            self._state.replied.add(source)
    _P_handler_316._labels = None
    _P_handler_316._notlabels = None

class Node_(da.NodeProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._events.extend([])
    _config_object = {'clock': 'Lamport'}

    def run(self):
        nprocs = (int(sys.argv[1]) if (len(sys.argv) > 1) else 10)
        nrounds = (int(sys.argv[2]) if (len(sys.argv) > 2) else 1)
        ps = self.new(P, num=nprocs)
        for p in ps:
            self._setup({p}, ((ps - {p}), nrounds))
        self._start(ps)