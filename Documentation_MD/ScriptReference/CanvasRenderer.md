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

# CanvasRenderer

class in UnityEngine

/

Inherits from:[Component](Component.html)

/

Implemented in:[UnityEngine.UIModule](UnityEngine.UIModule.html)

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

[ ]()

### Description

A component that will render to the screen after all normal rendering has
completed when attached to a [Canvas](Canvas.html). Designed for GUI
application.

Additional resources:[Canvas](Canvas.html).

### Properties

[absoluteDepth](CanvasRenderer-absoluteDepth.html)| Depth of the renderer
relative to the root canvas.  
---|---  
[clippingSoftness](CanvasRenderer-clippingSoftness.html)| The clipping
softness to apply to the renderer.  
[cull](CanvasRenderer-cull.html)| Indicates whether geometry emitted by this
renderer is ignored.  
[cullTransparentMesh](CanvasRenderer-cullTransparentMesh.html)| Indicates
whether geometry emitted by this renderer can be ignored when the vertex color
alpha is close to zero for every vertex of the mesh.  
[hasMoved](CanvasRenderer-hasMoved.html)| True if any change has occured that
would invalidate the positions of generated geometry.  
[hasPopInstruction](CanvasRenderer-hasPopInstruction.html)| Enable 'render
stack' pop draw call.  
[hasRectClipping](CanvasRenderer-hasRectClipping.html)| True if rect clipping
has been enabled on this renderer. Additional resources:
CanvasRenderer.EnableRectClipping, CanvasRenderer.DisableRectClipping.  
[materialCount](CanvasRenderer-materialCount.html)| The number of materials
usable by this renderer.  
[popMaterialCount](CanvasRenderer-popMaterialCount.html)| The number of
materials usable by this renderer. Used internally for masking.  
[relativeDepth](CanvasRenderer-relativeDepth.html)| Depth of the renderer
realative to the parent canvas.  
  
### Public Methods

[Clear](CanvasRenderer.Clear.html)| Remove all cached vertices.  
---|---  
[DisableRectClipping](CanvasRenderer.DisableRectClipping.html)| Disables
rectangle clipping for this CanvasRenderer.  
[EnableRectClipping](CanvasRenderer.EnableRectClipping.html)| Enables rect
clipping on the CanvasRendered. Geometry outside of the specified rect will be
clipped (not rendered).  
[GetAlpha](CanvasRenderer.GetAlpha.html)| Get the current alpha of the
renderer.  
[GetColor](CanvasRenderer.GetColor.html)| Get the current color of the
renderer.  
[GetInheritedAlpha](CanvasRenderer.GetInheritedAlpha.html)| Get the final
inherited alpha calculated by including all the parent alphas from included
parent CanvasGroups.  
[GetMaterial](CanvasRenderer.GetMaterial.html)| Gets the current Material
assigned to the CanvasRenderer.  
[GetMesh](CanvasRenderer.GetMesh.html)| Returns the current mesh used to
render the canvas content into.  
[GetPopMaterial](CanvasRenderer.GetPopMaterial.html)| Gets the current
Material assigned to the CanvasRenderer. Used internally for masking.  
[SetAlpha](CanvasRenderer.SetAlpha.html)| Set the alpha of the renderer. Will
be multiplied with the UIVertex alpha and the Canvas alpha.  
[SetAlphaTexture](CanvasRenderer.SetAlphaTexture.html)| The Alpha Texture that
will be passed to the Shader under the _AlphaTex property.  
[SetColor](CanvasRenderer.SetColor.html)| Set the color of the renderer. Will
be multiplied with the UIVertex color and the Canvas color.  
[SetMaterial](CanvasRenderer.SetMaterial.html)| Set the material for the
canvas renderer. If a texture is specified then it will be used as the
'MainTex' instead of the material's 'MainTex'. Additional resources:
CanvasRenderer.materialCount, CanvasRenderer.SetTexture.  
[SetMesh](CanvasRenderer.SetMesh.html)| Sets the Mesh used by this renderer.
Note the Mesh must be read/write enabled.  
[SetPopMaterial](CanvasRenderer.SetPopMaterial.html)| Set the material for the
canvas renderer. Used internally for masking.  
[SetTexture](CanvasRenderer.SetTexture.html)| Sets the texture used by this
renderer's material.  
  
### Static Methods

[AddUIVertexStream](CanvasRenderer.AddUIVertexStream.html)| Take the Vertex
stream and split it corrisponding arrays (positions, colors, uv0s, uv1s,
normals and tangents).  
---|---  
[CreateUIVertexStream](CanvasRenderer.CreateUIVertexStream.html)| Convert a
set of vertex components into a stream of UIVertex.  
[SplitUIVertexStreams](CanvasRenderer.SplitUIVertexStreams.html)| Given a list
of UIVertex, split the stream into it's component types.  
  
### Events

[onRequestRebuild](CanvasRenderer-onRequestRebuild.html)| (Editor Only) Event
that gets fired whenever the data in the CanvasRenderer gets invalidated and
needs to be rebuilt.  
---|---  
  
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

