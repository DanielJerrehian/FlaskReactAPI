import React from "react";
import ClipLoader from "react-spinners/ClipLoader";

function LoadingData(props) {
    const { loading } = props
    return (
        <div style={{display: 'flex', justifyContent: 'center', marginTop: '5rem', marginBottom: '5rem'}}>
            <ClipLoader color="black" loading={loading} size={50} />
        </div>
    )
}

export default LoadingData