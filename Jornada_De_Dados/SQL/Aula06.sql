# SubQuery

SELECT product_id FROM (
SELECT product_id 
FROM (
	SELECT product_id, rank
	FROM (SELECT 
			product_id,
			SUM( det.quantity * det.unit_price * ( 1 - det.discount )) sold_value,
			RANK() OVER (ORDER BY SUM( det.quantity * det.unit_price * ( 1 - det.discount )) DESC) rank -- WINDOWS FUNCTION
		FROM order_details det
		GROUP BY det.product_id
		ORDER BY rank)
	WHERE rank <= 5 )
WHERE product_id BETWEEN 35 and 65 )
ORDER BY product_id DESC