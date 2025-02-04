[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/event-functions.html)
  * [中文](/cn/current/Manual/event-functions.html)
  * [日本語](/ja/current/Manual/event-functions.html)
  * [한국어](/kr/current/Manual/event-functions.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/event-functions.html)
  * [中文](/cn/current/Manual/event-functions.html)
  * [日本語](/ja/current/Manual/event-functions.html)
  * [한국어](/kr/current/Manual/event-functions.html)

  * [Scripting](scripting.html)
  * [Object-oriented development](object-oriented-development.html)
  * [Handling events](event-handling.html)
  * Event functions

[](event-handling.html)

Handling events

[](execution-order.html)

Order of execution for event functions

# Event functions

Event functions are a set of predefined callbacks that all
[MonoBehaviour](class-MonoBehaviour.html) script components can potentially
receive. The callbacks are triggered by various Unity Editor and Engine
events, including:

  * Regular frame and physics updates
  * Object lifecycle events, such as initialization and destruction of objects in a scene
  * UI events
  * Physics events

Implement the appropriate method signature in your `MonoBehaviour`-derived
class to allow your game objects to react to the source events.

Refer to the [MonoBehaviour](../ScriptReference/MonoBehaviour.html) Scripting
API reference page for a full list of the available callbacks, where they are
listed under **Messages**. The rest of this section gives an overview of some
of the key groups of event functions.

## Regular update events

A game is like an animation where the animation frames are generated on the
fly. A key concept in games programming is making changes to position, state,
and behavior of objects just before each frame is rendered. The
[Update](../ScriptReference/MonoBehaviour.Update.html) function is the main
place for this kind of code in Unity. `Update` is called before the frame is
rendered and also before animations are calculated.

    
    
    void Update() {
        float distance = speed * Time.deltaTime * Input.GetAxis("Horizontal");
        transform.Translate(Vector3.right * distance);
    }
    
    

The **physics engine** A system that simulates aspects of physical systems so
that objects can accelerate correctly and be affected by collisions, gravity
and other forces. [More info](PhysicsSection.html)  
See in [Glossary](Glossary.html#PhysicsEngine) also updates in discrete time
steps in a similar way to the frame rendering. A separate event function
called [FixedUpdate](../ScriptReference/MonoBehaviour.FixedUpdate.html) is
called just before each physics update. Since the physics updates and frame
updates don’t occur with the same frequency, you can get more accurate results
from physics code if you place it in the `FixedUpdate` function rather than
`Update`.

    
    
    void FixedUpdate() {
        Vector3 force = transform.forward * driveForce * Input.GetAxis("Vertical");
        rigidbody.AddForce(force);
    }
    
    

It’s also sometimes useful to make additional changes at a point after the
`Update` and `FixedUpdate` functions have been called for all objects in the
**scene** A Scene contains the environments and menus of your game. Think of
each unique Scene file as a unique level. In each Scene, you place your
environments, obstacles, and decorations, essentially designing and building
your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene), and after all animations have been
calculated. Some examples of this scenario are:

  * When a **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) should remain trained on a target
object. The adjustment to the camera’s orientation must be made after the
target object has moved.

  * When the script code should override the effect of an animation. For example, to make a character’s head look towards a target object in the scene.

The [LateUpdate](../ScriptReference/MonoBehaviour.LateUpdate.html) function
can be used for these kinds of situations.

    
    
    void LateUpdate() {
        Camera.main.transform.LookAt(target.transform);
    }
    
    

## Initialization events

It’s often useful to be able to call initialization code in advance of any
updates that occur during gameplay. The
[Start](../ScriptReference/MonoBehaviour.Start.html) function is called before
the first frame or physics update on an object. The
[Awake](../ScriptReference/MonoBehaviour.Awake.html) function is called for
each object in the scene at the time when the scene loads. Note that although
the various objects’ `Start` and `Awake` functions are called in arbitrary
order, all instances of `Awake` will have finished before the first `Start` is
called. This means that code in a `Start` function can make use of other
initializations previously carried out in the `Awake` phase.

## GUI events

Unity has a system for rendering GUI controls over the main action in the
scene and responding to clicks on these controls. This code is handled
somewhat differently from the normal frame update and so it should be placed
in the [OnGUI](../ScriptReference/MonoBehaviour.OnGUI.html) function, which
will be called periodically.

    
    
    void OnGUI() {
        GUI.Label(labelRect, "Game Over");
    }
    
    

You can also detect mouse events that occur over a **GameObject** The
fundamental object in Unity scenes, which can represent characters, props,
scenery, cameras, waypoints, and more. A GameObject’s functionality is defined
by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) as it appears in the scene. This
can be used for targeting weapons or displaying information about the
character currently under the mouse pointer. A set of event functions named
with the prefix `OnMouse` (e.g.,
[OnMouseOver](../ScriptReference/MonoBehaviour.OnMouseOver.html),
[OnMouseDown](../ScriptReference/MonoBehaviour.OnMouseDown.html)) allow a
script to react to user actions with the mouse. For example, if the mouse
button is pressed while the pointer is over a particular object then an
`OnMouseDown` function in that object’s script will be called if it exists.

## Physics events

The physics engine will report **collisions** A collision occurs when the
physics engine detects that the colliders of two GameObjects make contact or
overlap, when at least one has a Rigidbody component and is in motion. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision) against an object by calling event
functions on that object’s script. The
[OnCollisionEnter](../ScriptReference/MonoBehaviour.OnCollisionEnter.html),
[OnCollisionStay](../ScriptReference/MonoBehaviour.OnCollisionStay.html) and
[OnCollisionExit](../ScriptReference/MonoBehaviour.OnCollisionExit.html)
functions will be called as contact is made, held and broken. The
corresponding
[OnTriggerEnter](../ScriptReference/MonoBehaviour.OnTriggerEnter.html),
[OnTriggerStay](../ScriptReference/MonoBehaviour.OnTriggerStay.html) and
[OnTriggerExit](../ScriptReference/MonoBehaviour.OnTriggerExit.html) functions
will be called when the object’s **collider** An invisible shape that is used
to handle physical collisions for an object. A collider doesn’t need to be
exactly the same shape as the object’s mesh - a rough approximation is often
more efficient and indistinguishable in gameplay. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider) is configured as a Trigger (ie, a
collider that simply detects when something enters it rather than reacting
physically). These functions may be called several times in succession if more
than one contact is detected during the physics update and so a parameter is
passed to the function giving details of the collision (position, identity of
the incoming object, etc).

    
    
    void OnCollisionEnter(Collision collision) {
        if (collision.gameObject.tag == "Arrow") {
            ApplyDamage(10);
        }
    }
    
    

## Additional resources

  * [MonoBehaviour](class-MonoBehaviour.html)
  * [Execution order of event functions](execution-order.html)
  * [MonoBehaviour API reference](../ScriptReference/MonoBehaviour.html)

[](event-handling.html)

Handling events

[](execution-order.html)

Order of execution for event functions

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

