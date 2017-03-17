# image-thumbnails-demo
demo to show swift converting images to thumbnails in a directory , requires ImageMagick linux package

initial testing on a dual core (i7-3520m) laptop in the memory filesystem (/dev/shm ) and 42 photos showed some scaling :

   swift-t -n 2 :  18s
   swift-t -n 3 :  13s
   swift-t -n 4 :  13s
