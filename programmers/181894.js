function solution(arr) {
  var first2 = arr.indexOf(2);
  if (first2 === -1) return [-1];
  var last2 = arr.lastIndexOf(2);
  if (last2 === -1) return [2];

  return arr.slice(first2, last2 + 1);
}
