[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

# MonoBehaviour

class in UnityEngine

/

Inherits from:[Behaviour](Behaviour.html)

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[Switch to Manual](../Manual/class-MonoBehaviour.html "Go to MonoBehaviour
Component in the Manual")

### Description

MonoBehaviour is a base class that many Unity scripts derive from.

MonoBehaviour offers life cycle functions that make it easier to develop with
Unity.  
  
MonoBehaviours always exist as a [Component](Component.html) of a GameObject,
and can be instantiated with
[GameObject.AddComponent](GameObject.AddComponent.html). Objects that need to
exist independently of a GameObject should derive from
[ScriptableObject](ScriptableObject.html) instead.  
  
A MonoBehaviour can be deleted with [Object.Destroy](Object.Destroy.html) or
[Object.DestroyImmediate](Object.DestroyImmediate.html). When the parent
GameObject is destroyed all components are automatically deleted, including
MonoBehaviours.  
  
After the underlying component is destroyed, the C# object for the
MonoBehaviour remains in memory until garbage is collected. A MonoBehaviour in
this state acts as if it is null. For example, it returns true for a "obj ==
null" check. However, this class doesn't support the [null-conditional
operator ](https://docs.microsoft.com/en-us/dotnet/csharp/language-
reference/language-specification/expressions#null-conditional-operator)
(**?.**) and the [null-coalescing operator ](https://docs.microsoft.com/en-
us/dotnet/csharp/language-reference/language-specification/expressions#the-
null-coalescing-operator)(**??**).  
  
When a MonoBehaviour is serialized, the value of C# fields are included
according to Unity's Serialization rules. See [Script
Serialization](../Manual/script-serialization.html) for details. The
serialized data also includes internal properties, such as the reference to
the [MonoScript](MonoScript.html) that tracks the implementation class for the
object.  
  
For code samples, see the individual MonoBehaviour methods.  
  
**Note:** There is a checkbox for enabling or disabling MonoBehaviour in the
Unity Editor. It disables functions when unticked. If none of these functions
are present in the script, the Unity Editor does not display the checkbox. The
functions are:  
  
[Start](MonoBehaviour.Start.html)()  
[Update](MonoBehaviour.Update.html)()  
[FixedUpdate](MonoBehaviour.FixedUpdate.html)()  
[LateUpdate](MonoBehaviour.LateUpdate.html)()  
[OnGUI](MonoBehaviour.OnGUI.html)()  
[OnDisable](MonoBehaviour.OnDisable.html)()  
[OnEnable](MonoBehaviour.OnEnable.html)()  
  
Additional resources: The [Deactivating
GameObjects](../Manual/DeactivatingGameObjects.html) page in the manual.

### Properties

[destroyCancellationToken](MonoBehaviour-destroyCancellationToken.html)|
Cancellation token raised when the MonoBehaviour is destroyed (Read Only).  
---|---  
[didAwake](MonoBehaviour-didAwake.html)| Returns a boolean value which
represents if Awake was called.  
[didStart](MonoBehaviour-didStart.html)| Returns a boolean value which
represents if Start was called.  
[runInEditMode](MonoBehaviour-runInEditMode.html)| Allow a specific instance
of a MonoBehaviour to run in edit mode (only available in the editor).  
[useGUILayout](MonoBehaviour-useGUILayout.html)| Disabling this lets you skip
the GUI layout phase.  
  
### Public Methods

[CancelInvoke](MonoBehaviour.CancelInvoke.html)| Cancels all Invoke calls on
this MonoBehaviour.  
---|---  
[Invoke](MonoBehaviour.Invoke.html)| Invokes the method methodName in time
seconds.  
[InvokeRepeating](MonoBehaviour.InvokeRepeating.html)| Invokes the method
methodName in time seconds, then repeatedly every repeatRate seconds.  
[IsInvoking](MonoBehaviour.IsInvoking.html)| Is any invoke on methodName
pending?  
[StartCoroutine](MonoBehaviour.StartCoroutine.html)| Starts a Coroutine.  
[StopAllCoroutines](MonoBehaviour.StopAllCoroutines.html)| Stops all
coroutines running on this behaviour.  
[StopCoroutine](MonoBehaviour.StopCoroutine.html)| Stops the first coroutine
named methodName, or the coroutine stored in routine running on this
behaviour.  
  
### Static Methods

[print](MonoBehaviour-print.html)| Logs message to the Unity Console
(identical to Debug.Log).  
---|---  
  
### Messages

[Awake](MonoBehaviour.Awake.html)| Unity calls Awake when an enabled script
instance is being loaded.  
---|---  
[FixedUpdate](MonoBehaviour.FixedUpdate.html)| Frame-rate independent
MonoBehaviour.FixedUpdate message for physics calculations.  
[LateUpdate](MonoBehaviour.LateUpdate.html)| LateUpdate is called every frame,
if the Behaviour is enabled.  
[OnAnimatorIK](MonoBehaviour.OnAnimatorIK.html)| Callback for setting up
animation IK (inverse kinematics).  
[OnAnimatorMove](MonoBehaviour.OnAnimatorMove.html)| Callback for processing
animation movements for modifying root motion.  
[OnApplicationFocus](MonoBehaviour.OnApplicationFocus.html)| Sent to all
GameObjects when the player gets or loses focus.  
[OnApplicationPause](MonoBehaviour.OnApplicationPause.html)| Sent to all
GameObjects when the playing application pauses or resumes on losing or
regaining focus.  
[OnApplicationQuit](MonoBehaviour.OnApplicationQuit.html)| Sent to all
GameObjects before the application quits.  
[OnAudioFilterRead](MonoBehaviour.OnAudioFilterRead.html)| If
OnAudioFilterRead is implemented, Unity will insert a custom filter into the
audio DSP chain.  
[OnBecameInvisible](MonoBehaviour.OnBecameInvisible.html)| OnBecameInvisible
is called when the renderer is no longer visible by any camera.  
[OnBecameVisible](MonoBehaviour.OnBecameVisible.html)| OnBecameVisible is
called when the renderer became visible by any camera.  
[OnCollisionEnter](MonoBehaviour.OnCollisionEnter.html)| OnCollisionEnter is
called when this collider/rigidbody has begun touching another
rigidbody/collider.  
[OnCollisionEnter2D](MonoBehaviour.OnCollisionEnter2D.html)| Sent when an
incoming collider makes contact with this object's collider (2D physics only).  
[OnCollisionExit](MonoBehaviour.OnCollisionExit.html)| OnCollisionExit is
called when this collider/rigidbody has stopped touching another
rigidbody/collider.  
[OnCollisionExit2D](MonoBehaviour.OnCollisionExit2D.html)| Sent when a
collider on another object stops touching this object's collider (2D physics
only).  
[OnCollisionStay](MonoBehaviour.OnCollisionStay.html)| OnCollisionStay is
called once per frame for every Collider or Rigidbody that touches another
Collider or Rigidbody.  
[OnCollisionStay2D](MonoBehaviour.OnCollisionStay2D.html)| Sent each frame
where a collider on another object is touching this object's collider (2D
physics only).  
[OnConnectedToServer](MonoBehaviour.OnConnectedToServer.html)| Called on the
client when you have successfully connected to a server.  
[OnControllerColliderHit](MonoBehaviour.OnControllerColliderHit.html)|
OnControllerColliderHit is called when the controller hits a collider while
performing a Move.  
[OnDestroy](MonoBehaviour.OnDestroy.html)| Destroying the attached Behaviour
will result in the game or Scene receiving OnDestroy.  
[OnDisable](MonoBehaviour.OnDisable.html)| This function is called when the
behaviour becomes disabled.  
[OnDrawGizmos](MonoBehaviour.OnDrawGizmos.html)| Implement OnDrawGizmos if you
want to draw gizmos that are also pickable and always drawn.  
[OnDrawGizmosSelected](MonoBehaviour.OnDrawGizmosSelected.html)| Implement
OnDrawGizmosSelected to draw a gizmo if the object is selected.  
[OnEnable](MonoBehaviour.OnEnable.html)| This function is called when the
object becomes enabled and active.  
[OnFailedToConnect](MonoBehaviour.OnFailedToConnect.html)| Called on the
client when a connection attempt fails for some reason.  
[OnGUI](MonoBehaviour.OnGUI.html)| OnGUI is called for rendering and handling
GUI events.  
[OnJointBreak](MonoBehaviour.OnJointBreak.html)| Called when a joint attached
to the same game object broke.  
[OnJointBreak2D](MonoBehaviour.OnJointBreak2D.html)| Called when a Joint2D
attached to the same game object breaks.  
[OnMouseDown](MonoBehaviour.OnMouseDown.html)|  OnMouseDown is called when the
user presses the left mouse button while over the Collider.  
[OnMouseDrag](MonoBehaviour.OnMouseDrag.html)| OnMouseDrag is called when the
user has clicked on a Collider and is still holding down the mouse.  
[OnMouseEnter](MonoBehaviour.OnMouseEnter.html)| Called when the mouse enters
the Collider.  
[OnMouseExit](MonoBehaviour.OnMouseExit.html)| Called when the mouse is not
any longer over the Collider.  
[OnMouseOver](MonoBehaviour.OnMouseOver.html)| Called every frame while the
mouse is over the Collider.  
[OnMouseUp](MonoBehaviour.OnMouseUp.html)| OnMouseUp is called when the user
has released the mouse button.  
[OnMouseUpAsButton](MonoBehaviour.OnMouseUpAsButton.html)| OnMouseUpAsButton
is only called when the mouse is released over the same Collider as it was
pressed.  
[OnParticleCollision](MonoBehaviour.OnParticleCollision.html)|
OnParticleCollision is called when a particle hits a Collider.  
[OnParticleSystemStopped](MonoBehaviour.OnParticleSystemStopped.html)|
OnParticleSystemStopped is called when all particles in the system have died,
and no new particles will be born. New particles cease to be created either
after Stop is called, or when the duration property of a non-looping system
has been exceeded.  
[OnParticleTrigger](MonoBehaviour.OnParticleTrigger.html)| OnParticleTrigger
is called when any particles in a Particle System meet the conditions in the
trigger module.  
[OnParticleUpdateJobScheduled](MonoBehaviour.OnParticleUpdateJobScheduled.html)|
OnParticleUpdateJobScheduled is called when a Particle System's built-in
update job has been scheduled.  
[OnPostRender](MonoBehaviour.OnPostRender.html)|  Event function that Unity
calls after a Camera renders the scene.  
[OnPreCull](MonoBehaviour.OnPreCull.html)|  Event function that Unity calls
before a Camera culls the scene.  
[OnPreRender](MonoBehaviour.OnPreRender.html)|  Event function that Unity
calls before a Camera renders the scene.  
[OnRenderImage](MonoBehaviour.OnRenderImage.html)|  Event function that Unity
calls after a Camera has finished rendering, that allows you to modify the
Camera's final image.  
[OnRenderObject](MonoBehaviour.OnRenderObject.html)| OnRenderObject is called
after camera has rendered the Scene.  
[OnServerInitialized](MonoBehaviour.OnServerInitialized.html)| Called on the
server whenever a Network.InitializeServer was invoked and has completed.  
[OnTransformChildrenChanged](MonoBehaviour.OnTransformChildrenChanged.html)|
This function is called when the list of children of the transform of the
GameObject has changed.  
[OnTransformParentChanged](MonoBehaviour.OnTransformParentChanged.html)| This
function is called when a direct or indirect parent of the transform of the
GameObject has changed.  
[OnTriggerEnter](MonoBehaviour.OnTriggerEnter.html)| When a GameObject
collides with another GameObject, Unity calls OnTriggerEnter.  
[OnTriggerEnter2D](MonoBehaviour.OnTriggerEnter2D.html)| Sent when another
object enters a trigger collider attached to this object (2D physics only).  
[OnTriggerExit](MonoBehaviour.OnTriggerExit.html)| OnTriggerExit is called
when the Collider other has stopped touching the trigger.  
[OnTriggerExit2D](MonoBehaviour.OnTriggerExit2D.html)| Sent when another
object leaves a trigger collider attached to this object (2D physics only).  
[OnTriggerStay](MonoBehaviour.OnTriggerStay.html)| OnTriggerStay is called
once per physics update for every Collider other that is touching the trigger.  
[OnTriggerStay2D](MonoBehaviour.OnTriggerStay2D.html)| Sent once per physics
update when another object is within a trigger collider attached to this
object (2D physics only).  
[OnValidate](MonoBehaviour.OnValidate.html)| Editor-only function that Unity
calls when the script is loaded or a value changes in the Inspector.  
[OnWillRenderObject](MonoBehaviour.OnWillRenderObject.html)|
OnWillRenderObject is called for each camera if the object is visible and not
a UI element.  
[Reset](MonoBehaviour.Reset.html)| Reset to default values.  
[Start](MonoBehaviour.Start.html)| Start is called on the frame when a script
is enabled just before any of the Update methods are called the first time.  
[Update](MonoBehaviour.Update.html)| Update is called every frame, if the
MonoBehaviour is enabled.  
  
### Inherited Members

### Properties

[enabled](Behaviour-enabled.html)| Enabled Behaviours are Updated, disabled
Behaviours are not.  
---|---  
[isActiveAndEnabled](Behaviour-isActiveAndEnabled.html)| Reports whether a
GameObject and its associated Behaviour is active and enabled.  
[gameObject](Component-gameObject.html)| The game object this component is
attached to. A component is always attached to a game object.  
[tag](Component-tag.html)| The tag of this game object.  
[transform](Component-transform.html)| The Transform attached to this
GameObject.  
[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[BroadcastMessage](Component.BroadcastMessage.html)| Calls the method named
methodName on every MonoBehaviour in this game object or any of its children.  
---|---  
[CompareTag](Component.CompareTag.html)| Checks the GameObject's tag against
the defined tag.  
[GetComponent](Component.GetComponent.html)| Gets a reference to a component
of type T on the same GameObject as the component specified.  
[GetComponentInChildren](Component.GetComponentInChildren.html)| Gets a
reference to a component of type T on the same GameObject as the component
specified, or any child of the GameObject.  
[GetComponentIndex](Component.GetComponentIndex.html)| Gets the index of the
component on its parent GameObject.  
[GetComponentInParent](Component.GetComponentInParent.html)| Gets a reference
to a component of type T on the same GameObject as the component specified, or
any parent of the GameObject.  
[GetComponents](Component.GetComponents.html)| Gets references to all
components of type T on the same GameObject as the component specified.  
[GetComponentsInChildren](Component.GetComponentsInChildren.html)| Gets
references to all components of type T on the same GameObject as the component
specified, and any child of the GameObject.  
[GetComponentsInParent](Component.GetComponentsInParent.html)| Gets references
to all components of type T on the same GameObject as the component specified,
and any parent of the GameObject.  
[SendMessage](Component.SendMessage.html)| Calls the method named methodName
on every MonoBehaviour in this game object.  
[SendMessageUpwards](Component.SendMessageUpwards.html)| Calls the method
named methodName on every MonoBehaviour in this game object and on every
ancestor of the behaviour.  
[TryGetComponent](Component.TryGetComponent.html)| Gets the component of the
specified type, if it exists.  
[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
[ToString](Object.ToString.html)| Returns the name of the object.  
  
### Static Methods

[Destroy](Object.Destroy.html)| Removes a GameObject, component or asset.  
---|---  
[DestroyImmediate](Object.DestroyImmediate.html)| Destroys the object obj
immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](Object.DontDestroyOnLoad.html)| Do not destroy the target
Object when loading a new Scene.  
[FindAnyObjectByType](Object.FindAnyObjectByType.html)| Retrieves any active
loaded object of Type type.  
[FindFirstObjectByType](Object.FindFirstObjectByType.html)| Retrieves the
first active loaded object of Type type.  
[FindObjectsByType](Object.FindObjectsByType.html)| Retrieves a list of all
loaded objects of Type type.  
[Instantiate](Object.Instantiate.html)| Clones the object original and returns
the clone.  
[InstantiateAsync](Object.InstantiateAsync.html)| Captures a snapshot of the
original object (that must be related to some GameObject) and returns the
AsyncInstantiateOperation.  
  
### Operators

[bool](Object-operator_Object.html)| Does the object exist?  
---|---  
[operator !=](Object-operator_ne.html)| Compares if two objects refer to a
different object.  
[operator ==](Object-operator_eq.html)| Compares two object references to see
if they refer to the same object.  
  
Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

