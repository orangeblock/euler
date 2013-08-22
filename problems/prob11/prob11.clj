(use '[clojure.string :only [split split-lines]])

(defn strings-to-ints [strlist]
  "Convert the strlist to a vector of ints"
  (vec (map #(Integer/valueOf %) strlist)))

(def grid
  (vec (map #(strings-to-ints (split % #" "))
            (split-lines (slurp "grid.txt")))))

(defn row-products [grid x y]
  (for [r (range x (+ x 4))]
    (apply * (->> (get grid r) (drop y) (take 4)))))

(defn col-products [grid x y]
  (for [c (range y (+ y 4))]
    (apply * (->> (map #(nth % c) grid) (drop x) (take 4)))))

(defn diag-products [grid x y]
  (list
   (* (get-in grid [x y]) (get-in grid [(+ x 1) (+ y 1)]) (get-in grid [(+ x 2) (+ y 2)]) (get-in grid [(+ x 3) (+ y 3)]))
   (* (get-in grid [(+ x 3) y]) (get-in grid [(+ x 2) (+ y 1)]) (get-in grid [(+ x 1) (+ y 2)]) (get-in grid [x (+ y 3)]))))

(defn matrix-products [grid x y]
  "Return all the 4-element products in the 4x4 matrix with (x,y) as top-left corner."
  (concat
   (row-products grid x y)
   (col-products grid x y)
   (diag-products grid x y)))

(defn max-product [grid]
  (let [num-range (range (- (count grid) 4))]
    (->> (for [x num-range y num-range] (matrix-products grid x y))
         (apply concat)
         (apply max))))

(println (max-product grid))