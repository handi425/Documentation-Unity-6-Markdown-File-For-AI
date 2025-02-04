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

# ReflectionProbe

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

[Switch to Manual](../Manual/class-ReflectionProbe.html "Go to ReflectionProbe
Component in the Manual")

### Description

The reflection probe is used to capture the surroundings into a texture which
is passed to the shaders and used for reflections.

The properties are an exact match for the values shown in the Inspector.  
  
This class is a script interface for a [reflection probe](../Manual/class-
ReflectionProbe.html) component.  
  
Reflection probes are usually just created in the Editor, but sometimes you
might want to create a reflection probe from a script:

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class ProbeCreator
    {
        [[MenuItem](MenuItem.html)("[ReflectionProbe](ReflectionProbe.html)/CreateRealtimeProbe")]
        public static void RealtimeProbe()
        {
            // Add a [GameObject](GameObject.html) with a [ReflectionProbe](ReflectionProbe.html) component
            [GameObject](GameObject.html) probeGameObject = new [GameObject](GameObject.html)("Realtime Reflection Probe");
            [ReflectionProbe](ReflectionProbe.html) probeComponent = probeGameObject.AddComponent<[ReflectionProbe](ReflectionProbe.html)>();
            
            // The probe will contribute to reflections inside a box of size 10x10x10 centered on the position of the probe
            probeComponent.size = new [Vector3](Vector3.html)(10, 10, 10);  
      
            // Set the type to realtime and refresh the probe every frame
            probeComponent.mode = UnityEngine.Rendering.ReflectionProbeMode.Realtime;
            probeComponent.refreshMode = UnityEngine.Rendering.ReflectionProbeRefreshMode.EveryFrame;
        }
    }
    

### Static Properties

[defaultTexture](ReflectionProbe-defaultTexture.html)| The surface texture of
the default reflection probe that captures the environment contribution. Read
only.  
---|---  
[defaultTextureHDRDecodeValues](ReflectionProbe-
defaultTextureHDRDecodeValues.html)| HDR decode values of the default
reflection probe texture.  
  
### Properties

[backgroundColor](ReflectionProbe-backgroundColor.html)| The color with which
the texture of reflection probe will be cleared.  
---|---  
[bakedTexture](ReflectionProbe-bakedTexture.html)| Reference to the baked
texture of the reflection probe's surrounding.  
[blendDistance](ReflectionProbe-blendDistance.html)| Distance around probe
used for blending (used in deferred probes).  
[bounds](ReflectionProbe-bounds.html)| The probe's world space axis-aligned
bounding box in which the probe can contribute to reflections (Read Only).  
[boxProjection](ReflectionProbe-boxProjection.html)| Should this reflection
probe use box projection?  
[center](ReflectionProbe-center.html)| The center of the probe's bounding box
in which the probe can contribute to reflections. The center is relative to
the position of the probe.  
[clearFlags](ReflectionProbe-clearFlags.html)| How the reflection probe clears
the background.  
[cullingMask](ReflectionProbe-cullingMask.html)| This is used to render parts
of the reflecion probe's surrounding selectively.  
[customBakedTexture](ReflectionProbe-customBakedTexture.html)| Reference to
the baked texture of the reflection probe's surrounding. Use this to assign
custom reflection texture.  
[farClipPlane](ReflectionProbe-farClipPlane.html)| The far clipping plane
distance when rendering the probe.  
[hdr](ReflectionProbe-hdr.html)| Should this reflection probe use HDR
rendering?  
[importance](ReflectionProbe-importance.html)| Reflection probe importance.  
[intensity](ReflectionProbe-intensity.html)| The intensity modifier that is
applied to the texture of reflection probe in the shader.  
[mode](ReflectionProbe-mode.html)| Should reflection probe texture be
generated in the Editor (ReflectionProbeMode.Baked) or should probe use custom
specified texure (ReflectionProbeMode.Custom)?  
[nearClipPlane](ReflectionProbe-nearClipPlane.html)| The near clipping plane
distance when rendering the probe.  
[realtimeTexture](ReflectionProbe-realtimeTexture.html)| Reference to the
real-time texture of the reflection probe's surroundings. Use this to assign a
RenderTexture to use for real-time reflection.  
[refreshMode](ReflectionProbe-refreshMode.html)| Sets the way the probe will
refresh.Additional resources: ReflectionProbeRefreshMode.  
[renderDynamicObjects](ReflectionProbe-renderDynamicObjects.html)| Specifies
whether Unity should render non-static GameObjects into the Reflection Probe.
If you set this to true, Unity renders non-static GameObjects into the
Reflection Probe. If you set this to false, Unity does not render non-static
GameObjects into the Reflection Probe. Unity only takes this property into
account if the Reflection Probe's Type is Custom.  
[resolution](ReflectionProbe-resolution.html)| Resolution of the underlying
reflection texture in pixels.  
[shadowDistance](ReflectionProbe-shadowDistance.html)| Shadow drawing distance
when rendering the probe.  
[size](ReflectionProbe-size.html)| The size of the probe's bounding box in
which the probe can contribute to reflections. The size is in world space.  
[texture](ReflectionProbe-texture.html)| Texture which is passed to the shader
of the objects in the vicinity of the reflection probe (Read Only).  
[textureHDRDecodeValues](ReflectionProbe-textureHDRDecodeValues.html)| HDR
decode values of the reflection probe texture.  
[timeSlicingMode](ReflectionProbe-timeSlicingMode.html)| Sets this probe time-
slicing modeAdditional resources: ReflectionProbeTimeSlicingMode.  
  
### Public Methods

[IsFinishedRendering](ReflectionProbe.IsFinishedRendering.html)| Checks if a
probe has finished a time-sliced render.  
---|---  
[RenderProbe](ReflectionProbe.RenderProbe.html)| Refreshes the probe's
cubemap.  
[Reset](ReflectionProbe.Reset.html)| Revert all ReflectionProbe parameters to
default.  
  
### Static Methods

[BlendCubemap](ReflectionProbe.BlendCubemap.html)| Utility method to blend 2
cubemaps into a target render texture.  
---|---  
[UpdateCachedState](ReflectionProbe.UpdateCachedState.html)| Updates the
culling system with the ReflectionProbe's current state. This ensures that
Unity correctly culls the ReflectionProbe during rendering if you implement
your own runtime reflection system.  
  
### Events

[defaultReflectionSet](ReflectionProbe-defaultReflectionSet.html)| Adds a
delegate to get notifications when the default specular Cubemap is changed.  
---|---  
[defaultReflectionTexture](ReflectionProbe-defaultReflectionTexture.html)|
Adds a delegate to get notifications when the default specular Cubemap is
changed.  
[reflectionProbeChanged](ReflectionProbe-reflectionProbeChanged.html)| Adds a
delegate to get notifications when a Reflection Probe is added to a Scene or
removed from a Scene.  
  
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

