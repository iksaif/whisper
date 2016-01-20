import whisper
import os
import time

def basic(compression):
    """Basic whisper benchmark."""
    retention = [(1, 60), (60, 60), (3600, 24), (86400, 365)]
    filename = 'test.wsp.' + compression
    whisper.create(filename, retention, compression=compression)

    updates = 10000
    now = time.time()
    for i in xrange(updates):
        timestamp = now - i
        whisper.update(filename, i, timestamp)
    os.unlink(filename)


if __name__ == '__main__':
    import timeit
    iterations = 10
    for compression in (whisper.NO_COMPRESSION,
                        whisper.ZLIB_COMPRESSION):
        result = timeit.timeit("basic('%s')" % compression,
                               setup="from __main__ import basic",
                               number=iterations)
        print '%s: %s' % (compression, result)
