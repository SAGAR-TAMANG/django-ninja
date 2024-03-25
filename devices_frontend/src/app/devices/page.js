async function getData() {
  const res = await fetch('http://127.0.0.1:8000/api/devices')
 
  if (!res.ok) {
    // This will activate the closest `error.js` Error Boundary
    throw new Error('Failed to fetch data')
  }
 
  return res.json()
}

export default async function Devices () {
  const devices = await getData()
  
  return (
    <div className="flex flex-col items-center mt-2">
      <h1 className="text-4xl">My Devices</h1>

      <div className="mt-5 flex flex-col gap-2">
        { devices.map(devices => <p className="text-xl" key={devices.id}> {devices.name} </p>)}
      </div>
    </div>
  )
}