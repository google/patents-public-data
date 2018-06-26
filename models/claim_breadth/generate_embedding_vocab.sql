#standardSQL
SELECT
  SUBSTR(cpc.code, 1, 4) cpc4 # Trim CPC Code to first 4 digits.
FROM
  `patents-public-data.patents.publications`,
  UNNEST(cpc) AS cpc
WHERE
  country_code = 'US'
  AND SUBSTR(cpc.code, 1, 1) IN ('D', 'E', 'G', 'H')
  AND FLOOR(priority_date / 10000) > 1995
GROUP BY
  1
HAVING
  COUNT(publication_number) > 3000
