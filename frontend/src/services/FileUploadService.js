const uploadFile = async (formData) => {
    try {
      const endPoint = "http://localhost:8000/uploadfile";
      const response = await fetch(endPoint, {
        method: 'POST',
        body: formData
      });
  
      if (response.ok) {
        const result = await response.json(); // assuming the server responds with JSON
        console.log(result);
        return result;
      } else {
        console.log("Failed to upload file");
        throw new Error(`File upload failed with status ${response.status}`);
      }
    } catch (error) {
    //   console.error(error);
    console.log("erorr--------------------------------");
      throw error;
    }
  };
  
  export default uploadFile;
  