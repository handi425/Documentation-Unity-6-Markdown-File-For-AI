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

# LineRenderer

class in UnityEngine

/

Inherits from:[Renderer](Renderer.html)

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

[Switch to Manual](../Manual/class-LineRenderer.html "Go to LineRenderer
Component in the Manual")

### Description

The line renderer is used to draw free-floating lines in 3D space.

This class is a script interface for a [line renderer](../Manual/class-
LineRenderer.html) component.

### Properties

[alignment](LineRenderer-alignment.html)| Select whether the line will face
the camera, or the orientation of the Transform Component.  
---|---  
[colorGradient](LineRenderer-colorGradient.html)| Set the color gradient
describing the color of the line at various points along its length.  
[endColor](LineRenderer-endColor.html)| Set the color at the end of the line.  
[endWidth](LineRenderer-endWidth.html)| Set the width at the end of the line.  
[generateLightingData](LineRenderer-generateLightingData.html)| Configures a
line to generate Normals and Tangents. With this data, Scene lighting can
affect the line via Normal Maps and the Unity Standard Shader, or your own
custom-built Shaders.  
[loop](LineRenderer-loop.html)| Connect the start and end positions of the
line together to form a continuous loop.  
[maskInteraction](LineRenderer-maskInteraction.html)| Specifies how the
LineRenderer interacts with SpriteMask.  
[numCapVertices](LineRenderer-numCapVertices.html)| Set this to a value
greater than 0, to get rounded corners on each end of the line. The default is
0.  
[numCornerVertices](LineRenderer-numCornerVertices.html)| Set this to a value
greater than 0, to get rounded corners between each segment of the line.  
[positionCount](LineRenderer-positionCount.html)| Set/get the number of
vertices.  
[shadowBias](LineRenderer-shadowBias.html)| Apply a shadow bias to prevent
self-shadowing artifacts. The specified value is the proportion of the line
width at each segment.  
[startColor](LineRenderer-startColor.html)| Set the color at the start of the
line.  
[startWidth](LineRenderer-startWidth.html)| Set the width at the start of the
line.  
[textureMode](LineRenderer-textureMode.html)| Choose whether the U coordinate
of the line texture is tiled or stretched.  
[textureScale](LineRenderer-textureScale.html)| A multiplier for the UV
coordinates of the line texture.  
[useWorldSpace](LineRenderer-useWorldSpace.html)| If enabled, the lines are
defined in world space.  
[widthCurve](LineRenderer-widthCurve.html)| Set the curve describing the width
of the line at various points along its length.  
[widthMultiplier](LineRenderer-widthMultiplier.html)| Set an overall
multiplier that is applied to the LineRenderer.widthCurve to get the final
width of the line.  
  
### Public Methods

[BakeMesh](LineRenderer.BakeMesh.html)| Creates a snapshot of LineRenderer and
stores it in mesh.  
---|---  
[GetPosition](LineRenderer.GetPosition.html)| Get the position of a vertex in
the line.  
[GetPositions](LineRenderer.GetPositions.html)| Get the positions of all
vertices in the line.  
[SetPosition](LineRenderer.SetPosition.html)| Set the position of a vertex in
the line.  
[SetPositions](LineRenderer.SetPositions.html)| Set the positions of all
vertices in the line.  
[Simplify](LineRenderer.Simplify.html)| Generates a simplified version of the
original line by removing points that fall within the specified tolerance.  
  
### Inherited Members

### Properties

[gameObject](Component-gameObject.html)| The game object this component is
attached to. A component is always attached to a game object.  
---|---  
[tag](Component-tag.html)| The tag of this game object.  
[transform](Component-transform.html)| The Transform attached to this
GameObject.  
[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
[name](Object-name.html)| The name of the object.  
[allowOcclusionWhenDynamic](Renderer-allowOcclusionWhenDynamic.html)| Controls
if dynamic occlusion culling should be performed for this renderer.  
[bounds](Renderer-bounds.html)| The bounding box of the renderer in world
space.  
[enabled](Renderer-enabled.html)| Makes the rendered 3D object visible if
enabled.  
[forceRenderingOff](Renderer-forceRenderingOff.html)| Allows turning off
rendering for a specific component.  
[isLOD0](Renderer-isLOD0.html)| Is the renderer the first LOD level in its
group.  
[isPartOfStaticBatch](Renderer-isPartOfStaticBatch.html)| Indicates whether
the renderer is part of a static batch with other renderers.  
[isVisible](Renderer-isVisible.html)| Is this renderer visible in any camera?
(Read Only)  
[lightmapIndex](Renderer-lightmapIndex.html)| The index of the baked lightmap
applied to this renderer.  
[lightmapScaleOffset](Renderer-lightmapScaleOffset.html)| The UV scale &
offset used for a lightmap.  
[lightProbeProxyVolumeOverride](Renderer-lightProbeProxyVolumeOverride.html)|
If set, the Renderer will use the Light Probe Proxy Volume component attached
to the source GameObject.  
[lightProbeUsage](Renderer-lightProbeUsage.html)| The light probe
interpolation type.  
[localBounds](Renderer-localBounds.html)| The bounding box of the renderer in
local space.  
[localToWorldMatrix](Renderer-localToWorldMatrix.html)| Matrix that transforms
a point from local space into world space (Read Only).  
[LODGroup](Renderer.LODGroup.html)| The LODGroup for this Renderer.  
[material](Renderer-material.html)| Returns the first instantiated Material
assigned to the renderer.  
[materials](Renderer-materials.html)| Returns all the instantiated materials
of this object.  
[motionVectorGenerationMode](Renderer-motionVectorGenerationMode.html)|
Specifies the mode for motion vector rendering.  
[probeAnchor](Renderer-probeAnchor.html)| If set, Renderer will use this
Transform's position to find the light or reflection probe.  
[rayTracingAccelerationStructureBuildFlags](Renderer-
rayTracingAccelerationStructureBuildFlags.html)| The flags Unity uses when it
builds acceleration structures associated with geometry used by renderers.  
[rayTracingAccelerationStructureBuildFlagsOverride](Renderer-
rayTracingAccelerationStructureBuildFlagsOverride.html)| Whether to override
the default build flags specified when creating a
RayTracingAccelerationStructure.  
[rayTracingMode](Renderer-rayTracingMode.html)| Describes how this renderer is
updated for ray tracing.  
[realtimeLightmapIndex](Renderer-realtimeLightmapIndex.html)| The index of the
real-time lightmap applied to this renderer.  
[realtimeLightmapScaleOffset](Renderer-realtimeLightmapScaleOffset.html)| The
UV scale & offset used for a real-time lightmap.  
[receiveShadows](Renderer-receiveShadows.html)| Does this object receive
shadows?  
[reflectionProbeUsage](Renderer-reflectionProbeUsage.html)| Should reflection
probes be used for this Renderer?  
[rendererPriority](Renderer-rendererPriority.html)| This value sorts renderers
by priority. Lower values are rendered first and higher values are rendered
last.  
[renderingLayerMask](Renderer-renderingLayerMask.html)| Determines which
rendering layer this renderer lives on, if you use a scriptable render
pipeline.  
[shadowCastingMode](Renderer-shadowCastingMode.html)| Does this object cast
shadows?  
[sharedMaterial](Renderer-sharedMaterial.html)| The shared material of this
object.  
[sharedMaterials](Renderer-sharedMaterials.html)| All the shared materials of
this object.  
[sortingLayerID](Renderer-sortingLayerID.html)| Unique ID of the Renderer's
sorting layer.  
[sortingLayerName](Renderer-sortingLayerName.html)| Name of the Renderer's
sorting layer.  
[sortingOrder](Renderer-sortingOrder.html)| Renderer's order within a sorting
layer.  
[staticShadowCaster](Renderer-staticShadowCaster.html)| Is this renderer a
static shadow caster?  
[worldToLocalMatrix](Renderer-worldToLocalMatrix.html)| Matrix that transforms
a point from world space into local space (Read Only).  
  
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
[GetClosestReflectionProbes](Renderer.GetClosestReflectionProbes.html)|
Returns an array of closest reflection probes with weights, weight shows how
much influence the probe has on the renderer, this value is also used when
blending between reflection probes occur.  
[GetMaterials](Renderer.GetMaterials.html)| Returns all the instantiated
materials of this object.  
[GetPropertyBlock](Renderer.GetPropertyBlock.html)| Get per-Renderer or per-
Material property block.  
[GetSharedMaterials](Renderer.GetSharedMaterials.html)| Returns all the shared
materials of this object.  
[HasPropertyBlock](Renderer.HasPropertyBlock.html)| Returns true if the
Renderer has a material property block attached via SetPropertyBlock.  
[ResetBounds](Renderer.ResetBounds.html)| Reset custom world space bounds.  
[ResetLocalBounds](Renderer.ResetLocalBounds.html)| Reset custom local space
bounds.  
[SetMaterials](Renderer.SetMaterials.html)| Assigns the shared materials of
this object using the list of materials provided.  
[SetPropertyBlock](Renderer.SetPropertyBlock.html)| Lets you set or clear per-
renderer or per-material parameter overrides.  
[SetSharedMaterials](Renderer.SetSharedMaterials.html)| Assigns the shared
materials of this object using the list of materials provided.  
  
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
  
### Messages

[OnBecameInvisible](Renderer.OnBecameInvisible.html)|  OnBecameInvisible is
called when the object is no longer visible by any camera.  
---|---  
[OnBecameVisible](Renderer.OnBecameVisible.html)|  OnBecameVisible is called
when the object became visible by any camera.  
  
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

