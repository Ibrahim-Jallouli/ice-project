# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.10
#
# <auto-generated>
#
# Generated from file `music3.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy

# Start of module Music3
_M_Music3 = Ice.openModule('Music3')
__name__ = 'Music3'

if '_t_ByteSeq' not in _M_Music3.__dict__:
    _M_Music3._t_ByteSeq = IcePy.defineSequence('::Music3::ByteSeq', (), IcePy._t_byte)

_M_Music3._t_MusicService3 = IcePy.defineValue('::Music3::MusicService3', Ice.Value, -1, (), False, True, None, ())

if 'MusicService3Prx' not in _M_Music3.__dict__:
    _M_Music3.MusicService3Prx = Ice.createTempClass()
    class MusicService3Prx(Ice.ObjectPrx):

        def play(self, fileName, context=None):
            return _M_Music3.MusicService3._op_play.invoke(self, ((fileName, ), context))

        def playAsync(self, fileName, context=None):
            return _M_Music3.MusicService3._op_play.invokeAsync(self, ((fileName, ), context))

        def begin_play(self, fileName, _response=None, _ex=None, _sent=None, context=None):
            return _M_Music3.MusicService3._op_play.begin(self, ((fileName, ), _response, _ex, _sent, context))

        def end_play(self, _r):
            return _M_Music3.MusicService3._op_play.end(self, _r)

        def stop(self, context=None):
            return _M_Music3.MusicService3._op_stop.invoke(self, ((), context))

        def stopAsync(self, context=None):
            return _M_Music3.MusicService3._op_stop.invokeAsync(self, ((), context))

        def begin_stop(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_Music3.MusicService3._op_stop.begin(self, ((), _response, _ex, _sent, context))

        def end_stop(self, _r):
            return _M_Music3.MusicService3._op_stop.end(self, _r)

        def storeMusicFile(self, fileData, fileName, context=None):
            return _M_Music3.MusicService3._op_storeMusicFile.invoke(self, ((fileData, fileName), context))

        def storeMusicFileAsync(self, fileData, fileName, context=None):
            return _M_Music3.MusicService3._op_storeMusicFile.invokeAsync(self, ((fileData, fileName), context))

        def begin_storeMusicFile(self, fileData, fileName, _response=None, _ex=None, _sent=None, context=None):
            return _M_Music3.MusicService3._op_storeMusicFile.begin(self, ((fileData, fileName), _response, _ex, _sent, context))

        def end_storeMusicFile(self, _r):
            return _M_Music3.MusicService3._op_storeMusicFile.end(self, _r)

        def deleteMusicFile(self, fileName, context=None):
            return _M_Music3.MusicService3._op_deleteMusicFile.invoke(self, ((fileName, ), context))

        def deleteMusicFileAsync(self, fileName, context=None):
            return _M_Music3.MusicService3._op_deleteMusicFile.invokeAsync(self, ((fileName, ), context))

        def begin_deleteMusicFile(self, fileName, _response=None, _ex=None, _sent=None, context=None):
            return _M_Music3.MusicService3._op_deleteMusicFile.begin(self, ((fileName, ), _response, _ex, _sent, context))

        def end_deleteMusicFile(self, _r):
            return _M_Music3.MusicService3._op_deleteMusicFile.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_Music3.MusicService3Prx.ice_checkedCast(proxy, '::Music3::MusicService3', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_Music3.MusicService3Prx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::Music3::MusicService3'
    _M_Music3._t_MusicService3Prx = IcePy.defineProxy('::Music3::MusicService3', MusicService3Prx)

    _M_Music3.MusicService3Prx = MusicService3Prx
    del MusicService3Prx

    _M_Music3.MusicService3 = Ice.createTempClass()
    class MusicService3(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::Music3::MusicService3')

        def ice_id(self, current=None):
            return '::Music3::MusicService3'

        @staticmethod
        def ice_staticId():
            return '::Music3::MusicService3'

        def play(self, fileName, current=None):
            raise NotImplementedError("servant method 'play' not implemented")

        def stop(self, current=None):
            raise NotImplementedError("servant method 'stop' not implemented")

        def storeMusicFile(self, fileData, fileName, current=None):
            raise NotImplementedError("servant method 'storeMusicFile' not implemented")

        def deleteMusicFile(self, fileName, current=None):
            raise NotImplementedError("servant method 'deleteMusicFile' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_Music3._t_MusicService3Disp)

        __repr__ = __str__

    _M_Music3._t_MusicService3Disp = IcePy.defineClass('::Music3::MusicService3', MusicService3, (), None, ())
    MusicService3._ice_type = _M_Music3._t_MusicService3Disp

    MusicService3._op_play = IcePy.Operation('play', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), ((), _M_Music3._t_ByteSeq, False, 0), ())
    MusicService3._op_stop = IcePy.Operation('stop', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, ())
    MusicService3._op_storeMusicFile = IcePy.Operation('storeMusicFile', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_Music3._t_ByteSeq, False, 0), ((), IcePy._t_string, False, 0)), (), None, ())
    MusicService3._op_deleteMusicFile = IcePy.Operation('deleteMusicFile', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), None, ())

    _M_Music3.MusicService3 = MusicService3
    del MusicService3

# End of module Music3