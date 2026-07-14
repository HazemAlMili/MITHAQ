# Baseline Performance Results

## Baseline Context

The baseline used the untouched P5.07 proxy Scene 01 before adding the representative gavel / seal / desk audit workload.

Production build baseline bundle:

- JavaScript chunk: approximately `993.17 KB`
- CSS chunk: approximately `3.91 KB`
- Build warning: JavaScript chunk exceeded Vite's 500 KB warning threshold

## Proxy Scene 01 Results

| Run | Average FPS | 1% Low FPS | p95 Frame Time | Console Errors | Canvas |
| --- | ---: | ---: | ---: | ---: | ---: |
| baseline-proxy-scene01-01 | 59.38 | 59.52 | 16.7 ms | 0 | 1 |
| baseline-proxy-scene01-02 | 60.41 | 59.52 | 16.7 ms | 0 | 1 |
| baseline-proxy-scene01-03 | 61.65 | 59.52 | 16.7 ms | 0 | 1 |

## Baseline Interpretation

The P5.07 proxy architecture was not the primary bottleneck in the local harness. The performance failure appeared after adding a more representative real-asset Scene 01 workload.

This distinction matters: P5.07 can remain accepted as an architecture proof, while P5.08 blocks real-time mobile Scene 01 approval.

