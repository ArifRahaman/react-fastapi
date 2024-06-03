// import React, { useState, useEffect } from 'react';
// import axios from 'axios';
// const About = () => {
//     const [userData, setUserData] = useState(null);
//     const [isEdit, setIsEdit] = useState(false);
//     const [editedData, setEditedData] = useState({});

//     useEffect(() => {
//         const storedData = localStorage.getItem("man");
//         if (storedData) {
//             try {
//                 setUserData(JSON.parse(storedData));
//             } catch (error) {
//                 console.error('Error parsing localStorage data:', error);
//             }
//         }
//     }, []);

//     const handleEditClick = () => {
//         setIsEdit(true);
//         setEditedData({ ...userData });
//     };

//     const handleEditSubmit = async (e) => {
//         e.preventDefault();
//         try {
//             const response = await axios.put('http://127.0.0.1:8000/update-user', editedData, {
//                 headers: { 'Content-Type': 'application/json' },
//             });

//             if (response.status === 200) {
//                 setUserData(response.data);
//                 setIsEdit(false);
//             } else {
//                 console.error('Error updating user data:', response.status, response.statusText);
//             }
//         } catch (error) {
//             console.error('Error during update:', error);
//         }
//     };

//     const handleInputChange = (e) => {
//         setEditedData({ ...editedData, [e.target.name]: e.target.value });
//     };

//     return (
//         <div>
//             {userData && (
//                 <div>
//                     <div className='bg-slate-100'>USERNAME: {userData.username}</div>
//                     <div className='bg-slate-100'>EMAIL: {userData.email}</div>
//                     <div className='bg-slate-100'>ID: {userData.id}</div>
//                     {userData.password && <div className='bg-slate-100'>PASSWORD: {userData.password}</div>}
//                     <button onClick={handleEditClick}>Edit</button>
//                     {isEdit && (
//                         <form onSubmit={handleEditSubmit}>
//                             <input
//                                 type="text"
//                                 name="username"
//                                 value={editedData.username}
//                                 onChange={handleInputChange}
//                             />
//                             <input
//                                 type="email"
//                                 name="email"
//                                 value={editedData.email}
//                                 onChange={handleInputChange}
//                             />
//                             {/* ... other fields if needed */}
//                             <button type="submit">Save Changes</button>
//                         </form>
//                     )}
//                 </div>
//             )}
//         </div>
//     );
// };

// export default About;


import React, { useState, useEffect } from 'react';
import axios from 'axios';

const About = () => {
    const [userData, setUserData] = useState(null);
    const [isEdit, setIsEdit] = useState(false);
    const [editedData, setEditedData] = useState({});

    useEffect(() => {
        const storedData = localStorage.getItem("man");
        if (storedData) {
            try {
                setUserData(JSON.parse(storedData));
            } catch (error) {
                console.error('Error parsing localStorage data:', error);
            }
        }
    }, []);

    const handleEditClick = () => {
        setIsEdit(true);
        setEditedData({ ...userData });
    };

    const handleEditSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.put('http://127.0.0.1:8000/update-user', editedData, {
                headers: { 'Content-Type': 'application/json' },
            });

            if (response.status === 200) {
                // Update localStorage
                localStorage.setItem("man", JSON.stringify(response.data));
                alert("Successfully Changed");
                setUserData(response.data);
                setIsEdit(false);
            } else {
                console.error('Error updating user data:', response.status, response.statusText);
            }
        } catch (error) {
            console.error('Error during update:', error);
        }
    };
    const handleInputChange = (e) => {
        setEditedData({ ...editedData, [e.target.name]: e.target.value });
    };

    return (
        <div className="flex justify-center items-center min-h-screen bg-gray-100">
            {userData && (
                <div className="bg-white shadow-lg rounded-lg p-6 max-w-md w-full">
                    <div className="text-2xl font-bold text-center mb-4">User Information</div>
                    <div className="bg-blue-100 p-4 mb-4 rounded">
                        <div className="text-gray-700 font-semibold">USERNAME: {userData.username}</div>
                    </div>
                    <div className="bg-blue-100 p-4 mb-4 rounded">
                        <div className="text-gray-700 font-semibold">EMAIL: {userData.email}</div>
                    </div>
                    {/* <div className="bg-blue-100 p-4 mb-4 rounded">
                        <div className="text-gray-700 font-semibold">ID: {userData.id}</div>
                    </div> */}
                    {userData.password && (
                        <div className="bg-blue-100 p-4 mb-4 rounded">
                            <div className="text-gray-700 font-semibold">PASSWORD: {userData.password}</div>
                        </div>
                    )}
                    <div className="flex justify-center">
                        <button onClick={handleEditClick} className="bg-green-500 text-white py-2 px-4 rounded hover:bg-green-600">Edit</button>
                    </div>
                    {isEdit && (
                        <form onSubmit={handleEditSubmit} className="mt-4">
                            <div className="mb-4">
                                <input
                                    type="text"
                                    name="username"
                                    value={editedData.username}
                                    onChange={handleInputChange}
                                    className="w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                                    placeholder="Username"
                                />
                            </div>
                            <div className="mb-4">
                                <input
                                    type="email"
                                    name="email"
                                    value={editedData.email}
                                    onChange={handleInputChange}
                                    className="w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                                    placeholder="Email"
                                />
                            </div>
                            {/* ... other fields if needed */}
                            <div className="flex justify-center">
                                <button type="submit" className="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600">Save Changes</button>
                            </div>
                        </form>
                    )}
                </div>
            )}
        </div>
    );
};

export default About;
