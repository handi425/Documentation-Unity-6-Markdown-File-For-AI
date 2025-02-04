[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/WheelColliderTutorial.html)
  * [中文](/cn/current/Manual/WheelColliderTutorial.html)
  * [日本語](/ja/current/Manual/WheelColliderTutorial.html)
  * [한국어](/kr/current/Manual/WheelColliderTutorial.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/WheelColliderTutorial.html)
  * [中文](/cn/current/Manual/WheelColliderTutorial.html)
  * [日本語](/ja/current/Manual/WheelColliderTutorial.html)
  * [한국어](/kr/current/Manual/WheelColliderTutorial.html)

  * [Physics](PhysicsSection.html)
  * [Built-in 3D Physics](PhysicsOverview.html)
  * [Collision](collision-section.html)
  * [Collider shapes](collider-shapes.html)
  * [Wheel colliders](wheel-colliders.html)
  * Create a car with Wheel colliders

[](wheel-colliders-suspension.html)

Wheel collider suspension

[](class-WheelCollider.html)

Wheel collider component reference

# Create a car with Wheel colliders

This tutorial takes you through the process of creating a basic functioning
four-wheeled car with the PhysX [Wheel collider](class-WheelCollider.html)A
special collider for grounded vehicles. It has built-in collision detection,
wheel physics, and a slip-based tire friction model. It can be used for
objects other than wheels, but it is specifically designed for vehicles with
wheels. [More info](class-WheelCollider.html)  
See in [Glossary](Glossary.html#WheelCollider).

The steps include:

  1. Prepare the project
  2. Prepare the car model
  3. Add the Wheel colliders, and set their position and radius
  4. Add scripts to control car behavior, including car movement and wheel rotation
  5. Test the car

## Prepare the project

To follow these instructions, you need:

  * A new empty scene
  * The demo car model (download: [car.fbx](../uploads/Main/car.fbx), imported into the open project
  * A ground surface for the car to travel across.

To create a ground surface:

  1. Create a plane **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) and rename it `Ground`. This plane
is the ground that the car drives on.

  2. Set its position to (0,0,0), and its scale to (100,1,100).

## Prepare the car model

First, place the Car model in the **Scene** A Scene contains the environments
and menus of your game. Think of each unique Scene file as a unique level. In
each Scene, you place your environments, obstacles, and decorations,
essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene):

  1. In the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](ProjectView.html)  
See in [Glossary](Glossary.html#Projectwindow), select the imported `Car`
asset.

  2. Extract the car model’s textures so that Unity can display them in the Scene. To do this, navigate to the [Import Settings](class-FBXImporter.html) in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window and do the following:

    1. Select **Materials**
    2. Select **Textures** > **Extract Textures**. In the file explorer that opens, save them in the `Assets` folder (the default location).
    3. Select **Apply**.
  3. Place the Car asset into the Scene, on or just above the Ground plane.

Take a look at the Car GameObject’s hierarchy in the Hierarchy window. There
is a root GameObject called `Car`, and child GameObjects for the car body
model and each wheel model.

Configure the car body for **collision** A collision occurs when the physics
engine detects that the colliders of two GameObjects make contact or overlap,
when at least one has a Rigidbody component and is in motion. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision):

  1. On the `Car` root GameObject, add a [Rigidbody](class-Rigidbody.html)A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](class-Rigidbody.html)  
See in [Glossary](Glossary.html#Rigidbody) component.

  2. Set the Rigidbody’s **Mass** to `1500``. This value defines the weight of the car in kilograms. It is a suitable weight for the Wheel collider’s default suspension settings. For more information, see [Wheel collider suspension: Mass and suspension values](wheel-colliders-suspension.html#mass-suspension-values).
  3. On the `Car Body` GameObject, add a [Mesh collider](class-MeshCollider.html)A free-form collider component which accepts a mesh reference to define its collision surface shape. [More info](class-MeshCollider.html)  
See in [Glossary](Glossary.html#MeshCollider) component.

  4. On the new **Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) **collider** An invisible shape that is
used to handle physical collisions for an object. A collider doesn’t need to
be exactly the same shape as the object’s mesh - a rough approximation is
often more efficient and indistinguishable in gameplay. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider) component, enable **Convex**.

## Add the Wheel colliders

To add Wheel colliders to the wheel models, you need to create four new
separate GameObjects at the same position as the wheel models (but not as
child GameObjects of the wheels).

A fast way to set this up at approximately the same position is to duplicate
the wheel GameObjects and then configure the new GameObject:

  1. Select all four wheel GameObjects.
  2. Duplicate the GameObjects (Ctrl/Cmd+D).
  3. Select all four duplicates and do the following: 
    1. Remove the **Mesh Renderer** A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](class-MeshRenderer.html)  
See in [Glossary](Glossary.html#MeshRenderer) and **Mesh Filter** A mesh
component that takes a mesh from your assets and passes it to the Mesh
Renderer for rendering on the screen. [More info](class-MeshFilter.html)  
See in [Glossary](Glossary.html#MeshFilter) components

    2. Add a Wheel collider component
  4. Rename the new Wheel collider GameObjects. By default, Unity gives duplicate GameObjects the same name and adds a number in parentheses; for example, `Wheel Back Left (1)`. For clarity, add the word “Collider” to the GameObject name instead; for example, `Wheel Back Left collider`.

The Car GameObject hierarchy should now look like this:

![The root Car GameObject and all child GameObjects, including the Car Body,
four wheel model GameObjects, and four Wheel collider
GameObjects.](../uploads/Main/wheel-collider-tutorial-hierarchy.png) The root
Car GameObject and all child GameObjects, including the Car Body, four wheel
model GameObjects, and four Wheel collider GameObjects.

Next, you need to adjust the Wheel colliders’ position and size to match the
wheel models.

When you select a Wheel collider, the **Scene view** An interactive view into
the world you are creating. You use the Scene View to select and position
scenery, characters, cameras, lights, and all other types of Game Object.
[More info](UsingTheSceneView.html)  
See in [Glossary](Glossary.html#SceneView) displays a
[gizmo](GizmosMenu.html)A graphic overlay associated with a GameObject in a
Scene, and displayed in the Scene View. Built-in scene tools such as the move
tool are Gizmos, and you can create custom Gizmos using textures or scripting.
Some Gizmos are only drawn when the GameObject is selected, while other Gizmos
are drawn by the Editor regardless of which GameObjects are selected. [More
info](GizmosMenu.html#GizmosIcons)  
See in [Glossary](Glossary.html#Gizmo) which provides a visualization of the
Wheel collider settings (see [Wheel collider visualization](wheel-colliders-
introduction.html#wheel-collider-visualization)). You can use the gizmo to
check the position and size of the Wheel collider against the position and
size of the wheel model.

To see the wheel orientation and the gizmo more clearly, set the Scene’s [Draw
mode](ViewModes.html) to **Wireframe** and the [Scene
orientation](SceneViewNavigation.html) to **Isometric**.

### Set the Wheel collider position

When you first add the Wheel colliders with the workflow described in Add
Wheel colliders, they are too low (in the Scene view, the Wheel collider
circle appears below the wheel model mesh). This is because the **Suspension
Distance** starts from these GameObjects’ positions, and extends downwards by
the distance specified in the **Suspension Distance** setting. The Scene view
visualization displays the **Suspension Distance** as an orange line down the
Y axis of the Wheel collider’s gizmo.

The green circle outline displays the wheel at the halfway point of the
suspension distance extents, and should be considered the wheel’s normal
position, when the car is not squashed down or raised up on its suspension.
Therefore the green outline of each Wheel collider needs to be centered over
its corresponding wheel mesh.

![The Wheel collider gizmo indicates the position of the Wheel collider in
relation to the wheel model. In this image, the Wheel collider is too large
and too low.](../uploads/Main/wheel-collider-tutorial-gizmo-before.png) The
Wheel collider gizmo indicates the position of the Wheel collider in relation
to the wheel model. In this image, the Wheel collider is too large and too
low.

To correct this, you need to move the WheelCollider GameObjects up (on the Y
axis) by half the value of the Wheel collider’s **Suspension Distance**. In
this example project, the **Suspension Distance** is 0.3 (the default value),
so you need to move the Wheel collider GameObjects up by 0.15 units.

Unity allows you to enter simple mathematical calculations into numeric
fields. You can use this to add to the Y axis value.

  1. Select all four Wheel collider GameObjects.
  2. In the Inspector, navigate to the Transform’s **Position** property.
  3. In the **Y** axis value, place the cursor at the end of the value. Add `+0.15` to the end of the value (for example, if the value is 0.5, the value should now read `0.5+0.15`).
  4. Press the Return key.

Unity applies +0.15 to the previous value, which moves the Wheel collider
GameObjects up the Y axis by 0.15 units.

The Wheel collider gizmo should now be perfectly centered on the wheel meshes:

![The Wheel collider gizmo indicates the position of the Wheel collider in
relation to the wheel model. In this image, the Wheel collider is centered
correctly in the wheel model.](../uploads/Main/wheel-collider-tutorial-gizmo-
correct-transform.png) The Wheel collider gizmo indicates the position of the
Wheel collider in relation to the wheel model. In this image, the Wheel
collider is centered correctly in the wheel model.

### Set the Wheel collider radius

When you first add the Wheel colliders with the workflow described in Add
Wheel colliders, they are too big (in the Scene view, the Wheel collider gizmo
is larger than the wheel model mesh).

To correct this accurately, you need to know the exact radius of the wheel
model. This information should be available from your 3D modeling software, or
from the technical artist who authored the model.

In this example project, the radius of the wheel model is 0.44.

  1. Select all four Wheel collider GameObjects
  2. In the Inspector, navigate to the Wheel collider component’s **Radius** property
  3. Set the **Radius** to `0.44`.

If the exact radius of a wheel model is unknown or unavailable, you can use
the Wheel collider gizmo to approximately match its radius to the model.
Alternatively, you can use a [Sphere collider](class-SphereCollider.html)A
sphere-shaped collider component that handles collisions for GameObjects like
balls or other things that can be roughly approximated as a sphere for the
purposes of physics. [More info](class-SphereCollider.html)  
See in [Glossary](Glossary.html#SphereCollider) to get the radius, because the
Sphere collider automatically resizes to encompass the mesh of its associated
model.

To get the radius with a Sphere collider:

  1. Select any wheel model GameObject.
  2. Add a Sphere collider.
  3. Take note of the Sphere collider’s **Radius** property value.
  4. Remove the Sphere collider.
  5. Select all four Wheel collider GameObjects.
  6. In the Inspector, navigate to the Wheel collider component’s **Radius** property.
  7. Set the Wheel collider **Radius** to the Sphere collider **Radius** value you noted.

The Wheel colliders should now exactly match the position and size of the
wheel models.

![Two Wheel collider gizmos indicate the position of the Wheel colliders in
relation to the wheel models. In this image, the Wheel colliders are centered
correctly in the wheel model, and their radius correctly matches the radius of
the wheel model.](../uploads/Main/wheel-collider-tutorial-gizmo-correct-
radius.png) Two Wheel collider gizmos indicate the position of the Wheel
colliders in relation to the wheel models. In this image, the Wheel colliders
are centered correctly in the wheel model, and their radius correctly matches
the radius of the wheel model.

## Add scripts to control car behavior

To control the car, you need to add **scripts** A piece of code that allows
you to create your own Components, trigger game events, modify Component
properties over time and respond to user input in any way you like. [More
info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) to the project that do the following:

  * **Control car movement** : Send steering, torque, and brake values to the Wheel colliders based on user input.
  * **Control wheel movement** : Move and rotate the wheel meshes according to each Wheel collider’s state.

In this example, we use two scripts to do this: `CarControl.cs` and
`WheelControl.cs`.

### Add control for car movement

Create a C# file named `CarControl.cs`, and paste in the code below:

    
    
    using UnityEngine;
    
    public class CarControl : MonoBehaviour
    {
        public float motorTorque = 2000;
        public float brakeTorque = 2000;
        public float maxSpeed = 20;
        public float steeringRange = 30;
        public float steeringRangeAtMaxSpeed = 10;
        public float centreOfGravityOffset = -1f;
    
        WheelControl[] wheels;
        Rigidbody rigidBody;
    
        // Start is called before the first frame update
        void Start()
        {
            rigidBody = GetComponent<Rigidbody>();
    
            // Adjust center of mass vertically, to help prevent the car from rolling
            rigidBody.centerOfMass += Vector3.up * centreOfGravityOffset;
    
            // Find all child GameObjects that have the WheelControl script attached
            wheels = GetComponentsInChildren<WheelControl>();
        }
    
        // Update is called once per frame
        void Update()
        {
    
            float vInput = Input.GetAxis("Vertical");
            float hInput = Input.GetAxis("Horizontal");
    
            // Calculate current speed in relation to the forward direction of the car
            // (this returns a negative number when traveling backwards)
            float forwardSpeed = Vector3.Dot(transform.forward, rigidBody.velocity);
    
    
            // Calculate how close the car is to top speed
            // as a number from zero to one
            float speedFactor = Mathf.InverseLerp(0, maxSpeed, forwardSpeed);
    
            // Use that to calculate how much torque is available 
            // (zero torque at top speed)
            float currentMotorTorque = Mathf.Lerp(motorTorque, 0, speedFactor);
    
            // …and to calculate how much to steer 
            // (the car steers more gently at top speed)
            float currentSteerRange = Mathf.Lerp(steeringRange, steeringRangeAtMaxSpeed, speedFactor);
    
            // Check whether the user input is in the same direction 
            // as the car's velocity
            bool isAccelerating = Mathf.Sign(vInput) == Mathf.Sign(forwardSpeed);
    
            foreach (var wheel in wheels)
            {
                // Apply steering to Wheel colliders that have "Steerable" enabled
                if (wheel.steerable)
                {
                    wheel.WheelCollider.steerAngle = hInput * currentSteerRange;
                }
                
                if (isAccelerating)
                {
                    // Apply torque to Wheel colliders that have "Motorized" enabled
                    if (wheel.motorized)
                    {
                        wheel.WheelCollider.motorTorque = vInput * currentMotorTorque;
                    }
                    wheel.WheelCollider.brakeTorque = 0;
                }
                else
                {
                    // If the user is trying to go in the opposite direction
                    // apply brakes to all wheels
                    wheel.WheelCollider.brakeTorque = Mathf.Abs(vInput) * brakeTorque;
                    wheel.WheelCollider.motorTorque = 0;
                }
            }
        }
    }
    

Add this `CarControl.cs` script to the `Car` root GameObject.

The `CarControl.cs` script handles car behavior such as acceleration, torque,
and braking, based on user input. See the code comments for details.

Some elements of the `CarControl.cs` script refer to the `WheelControl.cs`
script created in the next section.

### Add control for wheel movement

Create a C# file named `WheelControl.cs`, and paste in the code below:

    
    
    using UnityEngine;
    
    public class WheelControl : MonoBehaviour
    {
        public Transform wheelModel;
    
        [HideInInspector] public WheelCollider WheelCollider;
    
        // Create properties for the CarControl script
        // (You should enable/disable these via the 
        // Editor Inspector window)
        public bool steerable;
        public bool motorized;
    
        Vector3 position;
        Quaternion rotation;
    
        // Start is called before the first frame update
        private void Start()
        {
            WheelCollider = GetComponent<WheelCollider>();
        }
    
        // Update is called once per frame
        void Update()
        {
            // Get the Wheel collider's world pose values and
            // use them to set the wheel model's position and rotation
            WheelCollider.GetWorldPose(out position, out rotation);
            wheelModel.transform.position = position;
            wheelModel.transform.rotation = rotation;
        }
    }
    

Add this script to each Wheel collider GameObject.

The `WheelControl.cs` script uses
[`WheelCollider.GetWorldPose`](../ScriptReference/WheelCollider.GetWorldPose.html)
to get the Wheel collider’s position in the scene. The script then assigns
that position information to a specified wheel model GameObject. See the code
comments for details.

Each instance of the `WheelControl.cs` script must have a reference to its
corresponding wheel model GameObject.

To assign the correct wheel model GameObject to each Wheel collider:

  1. Select a Wheel collider GameObject
  2. In the Inspector window, navigate to the **Wheel Control** component created by the script
  3. Set the **Wheel Model** to the corresponding wheel model GameObject (for example, on the “Wheel Rear Left collider” GameObject, assign the “Wheel Rear Left” wheel model GameObject):
  4. Repeat for each Wheel collider.

You also need to select which wheels receive motor input and steering input
from the CarControl script. To simulate a four-wheel drive car via the Wheel
Control properties:

  1. On all four Wheel collider GameObjects, enable **Motorized**.
  2. On the two front Wheel collider GameObjects, enable **Steerable**.

## Test the car

To test the car, enter Play mode and use the arrow or WASD keys to move and
steer. Note that input controls only work when the Game view has focus.

To get a better view of the car moving around the Scene:

  1. Arrange the Editor windows so that both the Scene view and Game view are visible at the same time.
  2. Lock the Scene view’s focus to the car. To do this, select the `Car` root GameObject in the Scene view, then press Shift + F.

Now that you have a basic setup, you can try changing different settings to
observe how they affect the movement of the car. You can also follow these
instructions with different car models and observe the similarities and
differences in their setup.

[](wheel-colliders-suspension.html)

Wheel collider suspension

[](class-WheelCollider.html)

Wheel collider component reference

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

