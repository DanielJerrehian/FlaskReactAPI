import React from "react";
import ClipLoader from "react-spinners/ClipLoader";

function LoadingData(props) {
    const { loading } = props
    return (
        <ClipLoader color="black" loading={loading} size={75} />
    )
}

export default LoadingData