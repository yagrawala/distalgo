# -*- generated by 1.0.9 -*-
import da
PatternExpr_191 = da.pat.TuplePattern([da.pat.ConstantPattern('Out'), da.pat.SelfPattern(), da.pat.FreePattern('d')])
PatternExpr_231 = da.pat.TuplePattern([da.pat.ConstantPattern('Leader'), da.pat.FreePattern('leader')])
PatternExpr_259 = da.pat.TuplePattern([da.pat.ConstantPattern('In'), da.pat.SelfPattern()])
PatternExpr_266 = da.pat.BoundPattern('_BoundPattern267_')
PatternExpr_282 = da.pat.TuplePattern([da.pat.ConstantPattern('In'), da.pat.SelfPattern()])
PatternExpr_289 = da.pat.BoundPattern('_BoundPattern290_')
PatternExpr_311 = da.pat.TuplePattern([da.pat.ConstantPattern('Out'), da.pat.FreePattern('v'), da.pat.FreePattern('d')])
PatternExpr_320 = da.pat.FreePattern('source')
PatternExpr_357 = da.pat.TuplePattern([da.pat.ConstantPattern('In'), da.pat.FreePattern('v')])
PatternExpr_364 = da.pat.FreePattern('source')
PatternExpr_384 = da.pat.TuplePattern([da.pat.ConstantPattern('Leader'), da.pat.FreePattern('leader')])
PatternExpr_391 = da.pat.FreePattern('source')
PatternExpr_268 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.BoundPattern('_BoundPattern274_')]), da.pat.TuplePattern([da.pat.ConstantPattern('In'), da.pat.SelfPattern()])])
PatternExpr_291 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.BoundPattern('_BoundPattern297_')]), da.pat.TuplePattern([da.pat.ConstantPattern('In'), da.pat.SelfPattern()])])
_config_object = {}
import sys
import random

class P(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._PReceivedEvent_0 = []
        self._PReceivedEvent_1 = []
        self._PReceivedEvent_2 = []
        self._PReceivedEvent_3 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_0', PatternExpr_191, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_1', PatternExpr_231, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_2', PatternExpr_259, sources=[PatternExpr_266], destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_3', PatternExpr_282, sources=[PatternExpr_289], destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_4', PatternExpr_311, sources=[PatternExpr_320], destinations=None, timestamps=None, record_history=None, handlers=[self._P_handler_310]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_5', PatternExpr_357, sources=[PatternExpr_364], destinations=None, timestamps=None, record_history=None, handlers=[self._P_handler_356]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_6', PatternExpr_384, sources=[PatternExpr_391], destinations=None, timestamps=None, record_history=None, handlers=[self._P_handler_383])])

    def setup(self, left, right, **rest_487):
        super().setup(left=left, right=right, **rest_487)
        self._state.left = left
        self._state.right = right
        pass

    def run(self):
        distance = 1
        while True:
            self.send(('Out', self._id, distance), to={self._state.left, self._state.right})
            super()._label('_st_label_188', block=False)
            d = None

            def ExistentialOpExpr_189():
                nonlocal d
                for (_, _, (_ConstantPattern208_, _ConstantPattern210_, d)) in self._PReceivedEvent_0:
                    if (_ConstantPattern208_ == 'Out'):
                        if (_ConstantPattern210_ == self._id):
                            if True:
                                return True
                return False
            leader = None

            def ExistentialOpExpr_229():
                nonlocal leader
                for (_, _, (_ConstantPattern246_, leader)) in self._PReceivedEvent_1:
                    if (_ConstantPattern246_ == 'Leader'):
                        if True:
                            return True
                return False
            _st_label_188 = 0
            while (_st_label_188 == 0):
                _st_label_188 += 1
                if ExistentialOpExpr_189():
                    self.output(('I am leader at distance %d!' % d))
                    self.send(('Leader', self._id), to={self._state.left, self._state.right})
                    break
                    _st_label_188 += 1
                elif ExistentialOpExpr_229():
                    self.output('Leader is', leader)
                    break
                    _st_label_188 += 1
                elif (PatternExpr_268.match_iter(self._PReceivedEvent_2, _BoundPattern274_=self._state.left, SELF_ID=self._id) and PatternExpr_291.match_iter(self._PReceivedEvent_3, _BoundPattern297_=self._state.right, SELF_ID=self._id)):
                    distance *= 2
                    for attr in dir(self):
                        if (attr.find('ReceivedEvent_') != (- 1)):
                            getattr(self, attr).clear()
                    _st_label_188 += 1
                else:
                    super()._label('_st_label_188', block=True)
                    _st_label_188 -= 1
            else:
                if (_st_label_188 != 2):
                    continue
            if (_st_label_188 != 2):
                break

    def _P_handler_310(self, v, d, source):
        if (v > self._id):
            if (d > 1):
                self.send(('Out', v, (d - 1)), to=(self._state.right if (source == self._state.left) else self._state.left))
            elif (d == 1):
                self.send(('In', v), to=source)
    _P_handler_310._labels = None
    _P_handler_310._notlabels = None

    def _P_handler_356(self, v, source):
        if (v > self._id):
            self.send(('In', v), to=(self._state.right if (source == self._state.left) else self._state.left))
    _P_handler_356._labels = None
    _P_handler_356._notlabels = None

    def _P_handler_383(self, leader, source):
        self.send(('Leader', leader), to=(self._state.right if (source == self._state.left) else self._state.left))
    _P_handler_383._labels = None
    _P_handler_383._notlabels = None

class Node_(da.NodeProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._events.extend([])
    _config_object = {'channel': 'fifo'}

    def run(self):
        n = (int(sys.argv[1]) if (len(sys.argv) > 1) else 10)
        topology = list(self.new(P, num=n))
        random.shuffle(topology)
        for (i, p) in enumerate(topology):
            if (i == (len(topology) - 1)):
                self._setup({p}, (topology[(i - 1)], topology[0]))
            else:
                self._setup({p}, (topology[(i - 1)], topology[(i + 1)]))
        self._start(topology)