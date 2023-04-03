
import Data.List
-- module 001 where
sumDivisibleBy x = let n = div 999 x in x * (div ((n+1)*n) 2)

ans1 = sumDivisibleBy 3 + sumDivisibleBy 5 - sumDivisibleBy 15

-- Below is someone writing a program
ans2 = sum [n | n <- [1..1000-1], n `mod` 5 == 0 || n `mod` 3 == 0]
ans3 = sum (takeWhile (<10000) (filter odd (map (^2) [1..])))

largestDivisible :: Integer
largestDivisible = head (filter p [100000,99999..])
    where p x = x `mod` 3829 == 0

collatzSeq :: Int -> [Int]
collatzSeq 1 = [1]
collatzSeq x
      | even x = x : collatzSeq (div x 2)
      | odd  x = x : collatzSeq (x * 3 + 1)

clazLarger n = length(n) > 100

numLongChains :: Int
numLongChains = length(filter isLong (map collatzSeq [1..100]))
      where isLong xs = length xs > 30

numLongChains2 :: Int
numLongChains2 = length(filter (\xs -> length xs > 15) (map collatzSeq[1..100]))

sum' :: (Num a) => [a] -> a
sum' = sum
--sum' = foldl (+) 0

map' :: (a -> b) -> [a] -> [b]
map' f = foldr (\x acc -> f x : acc) []
--map' f xs = foldr (\x acc -> f x : acc) [] xs

sqrtSums :: Int
sqrtSums = length (takeWhile (<1000) (scanl1 (+) (map sqrt [1..]))) + 1

ans = map (negate. sum . tail) [[1..5], [3..6], [1..7]]

numUniques :: (Eq a) => [a] -> Int
numUniques = length . nub

wordNums :: String -> [(String, Int)]
wordNums = map (\ws -> (head ws, length ws)) . group .sort .words

isIn :: (Eq a) => [a] -> [a] -> Bool
needle `isIn` haystack = any (needle `isPrefixOf`) (tails haystack)
