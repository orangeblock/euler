(use '[clojure.string :only [split split-lines]])

(defn strings-to-ints [strlist]
  "Convert the strlist to a vector of ints"
  (vec (map #(Integer/valueOf %) strlist)))

(def grid
  (vec (map #(strings-to-ints (split % #" "))
            (split-lines (slurp "grid.txt")))))

(defn diag-products [grid x y]
  "Return the main and secondary diagonals of the 4x4 matrix with (x,y) as top left corner."
  (let [cell #((grid %1) %2)] ;cell accessor function
    (list
     (reduce * [(cell x y) (cell (+ x 1) (+ y 1)) (cell (+ x 2) (+ y 2)) (cell (+ x 3) (+ y 3))])
     (reduce * [(cell (+ x 3) y) (cell (+ x 2) (+ y 1)) (cell (+ x 1) (+ y 2)) (cell x (+ y 3))]))))

(defn matrix-products [grid x y]
  "Return all the possible, non-redundant 4-element products of the 4x4 matrix with (x,y) as top-left corner."
  (let [limit (- (count grid) 4)]
    (concat
     (if (<= y limit)
       (list (apply * (->> (grid x) (drop y) (take 4))))) ; add row product
     (if (<= x limit)
       (list (apply * (->> (map #(nth % y) grid) (drop x) (take 4))))) ; add col product
     (if (and (<= y limit) (<= x limit))
       (diag-products grid x y)))))

(defn max-product [grid]
  "Calculate the products starting from each cell of the matrix"
  (let [num-range (range (count grid))]
    (->> (for [x num-range y num-range] (matrix-products grid x y))
         (apply concat)
         (apply max))))

(println (max-product grid))
