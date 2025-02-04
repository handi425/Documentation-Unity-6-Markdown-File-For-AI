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

# BillboardAsset

class in UnityEngine

/

Inherits from:[Object](Object.html)

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

[Switch to Manual](../Manual/class-BillboardAsset.html "Go to BillboardAsset
Component in the Manual")

### Description

BillboardAsset describes how a billboard is rendered.

Billboards are a level-of-detail (LOD) method of drawing complicated 3D
objects in a simpler manner if they are further away. Because the object is
further away, there is often less requirement to draw the object at full
detail due to its size on-screen and low likelihood of being a focal point in
the Camera view. Instead, the object can be pre-rendered to a texture, and
this texture used on a very simple Camera-facing Mesh of flat geometry (often
simply a quadrilateral) known as a billboard. At great distances an object
does not significantly change its orientation relative to the camera, so a
billboard looks much like the object it represents from frame to frame,
without having to be redrawn from the model. The BillboardAsset class allows
the creation of billboards that are rendered from several directions, allowing
a BillboardAsset to efficiently represent an object at low level of detail
from any approximately-horizontal viewpoint.  
  
A BillboardAsset is usually created by importing SpeedTree assets. You can
also create your own once you know how the billboard is described.  
  
SpeedTree billboard geometry is usually more complex than a plain
quadrilateral. By using more vertices to cut out the empty part of the
billboard image, rendering performance can potentially be improved due to the
graphics system not having to draw as many redundant transparent pixels. You
have access to the geometry data via BillboardAsset.vertices and
BillboardAsset.indices.  
  
All vertices are considered in UV-space (see Fig. 1 below), because the
geometry is due to be textured by the billboard images. UV vertices are easily
expanded to 3D-space vertices by knowing the billboard's width, height,
bottom, and what direction the billboard is currently facing. Assuming we have
a billboard located at (0,0,0) looking at negative Z axis, the 3D-space
coordinates are calculated as:  
  
_X_ = (_u_ \- 0.5) * _width_  
_Y_ = _v_ * _height_ \+ _bottom_  
_Z_ = 0  
  
![](../StaticFiles/ScriptRefImages/Billboard_Geometry.png) Figure 1: How UV
vertices are expanded to 3D vertices  
  
In order to display something similar to the real 3D mesh being billboarded,
SpeedTree billboards select an appropriate image from several pre-rendered
images according to the current view direction. The images in Figure 2 below
are created by capturing the rendered image of the 3D tree at different view
angles, evenly distributed around the Y-axis. The first image always starts at
positive X axis direction (or 0° if you imagine a unit circle from above).  
  
![](../StaticFiles/ScriptRefImages/Billboard_Images.png) Figure 2: How the
eight billboard images are baked  
  
All images should be atlased together in one single texture. Each image is
represented as a [Vector4](Vector4.html) of {_left u_ , _top v_ , _width in u_
, _height in v_} in the atlas. You have access to all the images via
BillboardAsset.imageTexCoords. SpeedTree Modeler always exports a normal
texture alongside the diffuse texture for even better approximation of the
lighting, and it shares the same atlas layout with the diffuse texutre.  
  
Once the BillboardAsset is constructed, use
[BillboardRenderer](BillboardRenderer.html) to render it.

### Properties

[bottom](BillboardAsset-bottom.html)| Height of the billboard that is below
ground.  
---|---  
[height](BillboardAsset-height.html)| Height of the billboard.  
[imageCount](BillboardAsset-imageCount.html)| Number of pre-rendered images
that can be switched when the billboard is viewed from different angles.  
[indexCount](BillboardAsset-indexCount.html)| Number of indices in the
billboard mesh.  
[material](BillboardAsset-material.html)| The material used for rendering.  
[vertexCount](BillboardAsset-vertexCount.html)| Number of vertices in the
billboard mesh.  
[width](BillboardAsset-width.html)| Width of the billboard.  
  
### Constructors

[BillboardAsset](BillboardAsset-ctor.html)| Constructs a new BillboardAsset.  
---|---  
  
### Public Methods

[GetImageTexCoords](BillboardAsset.GetImageTexCoords.html)| Get the array of
billboard image texture coordinate data.  
---|---  
[GetIndices](BillboardAsset.GetIndices.html)| Get the indices of the billboard
mesh.  
[GetVertices](BillboardAsset.GetVertices.html)| Get the vertices of the
billboard mesh.  
[SetImageTexCoords](BillboardAsset.SetImageTexCoords.html)| Set the array of
billboard image texture coordinate data.  
[SetIndices](BillboardAsset.SetIndices.html)| Set the indices of the billboard
mesh.  
[SetVertices](BillboardAsset.SetVertices.html)| Set the vertices of the
billboard mesh.  
  
### Inherited Members

### Properties

[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
---|---  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
---|---  
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

