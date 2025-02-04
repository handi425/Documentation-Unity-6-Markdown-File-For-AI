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

#  [Mesh](Mesh.html).SetUVs

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

[Switch to Manual](../Manual/class-Mesh.html "Go to Mesh Component in the
Manual")

## Declaration

public void SetUVs(int channel, Vector2[] uvs);

## Declaration

public void SetUVs(int channel, Vector3[] uvs);

## Declaration

public void SetUVs(int channel, Vector4[] uvs);

## Declaration

public void SetUVs(int channel, List<Vector2> uvs);

## Declaration

public void SetUVs(int channel, List<Vector3> uvs);

## Declaration

public void SetUVs(int channel, List<Vector4> uvs);

## Declaration

public void SetUVs(int channel, NativeArray<T> uvs);

### Parameters

channel | The channel, in [0..7] range.  
---|---  
uvs | The UV data to set.  
  
### Description

Sets the texture coordinates (UVs) stored in a given channel.

Sets the UVs as a List of either [Vector2](Vector2.html),
[Vector3](Vector3.html), or [Vector4](Vector4.html). 2 dimensional (Vector2)
data is the most common use case, but 3 or 4 dimensional data is sometimes
used for special shader effects.  
  
Unity stores UVs in 0-1 space. [0,0] represents the bottom-left corner of the
texture, and [1,1] represents the top-right. Values are not clamped; you can
use values below 0 and above 1 if needed.  
  
A `channel` value of 0 corresponds to the channel that is commonly called
"UV0", and maps to the shader semantic `TEXCOORD0`. A `channel` value of 1
returns the channel that is commonly called "UV1", and maps to the shader
semantic `TEXCOORD1`. This continues up to and including a `channel` value of
7.  
  
By default, Unity uses the first channel (UV0) to store UVs for regular
textures such as diffuse maps and specular maps. Unity can use the second
channel (UV1) to store baked lightmap UVs, and the third channel (UV2) to
store input data for real-time lightmap UVs. For more information on lightmap
UVs and how Unity uses these channels, [Lightmap
UVs](../Manual/LightingGiUvs.html).  
  
**Note:** You can also access UV data using [uv](Mesh-uv.html) for UV0,
[uv2](Mesh-uv2.html) for UV1, [uv3](Mesh-uv3.html) for UV2, and so on up to
[uv8](Mesh-uv8.html). However, this older way of working is not recommended;
the properties are less user-friendly than this function and
[GetUVs](Mesh.GetUVs.html), and they also cause heap allocations.  
  
Additional resources: [GetUVs](Mesh.GetUVs.html).

* * *

## Declaration

public void SetUVs(int channel, Vector2[] uvs, int start, int length,
[Rendering.MeshUpdateFlags](Rendering.MeshUpdateFlags.html) flags =
MeshUpdateFlags.Default);

## Declaration

public void SetUVs(int channel, Vector3[] uvs, int start, int length,
[Rendering.MeshUpdateFlags](Rendering.MeshUpdateFlags.html) flags =
MeshUpdateFlags.Default);

## Declaration

public void SetUVs(int channel, Vector4[] uvs, int start, int length,
[Rendering.MeshUpdateFlags](Rendering.MeshUpdateFlags.html) flags =
MeshUpdateFlags.Default);

## Declaration

public void SetUVs(int channel, List<Vector2> uvs, int start, int length,
[Rendering.MeshUpdateFlags](Rendering.MeshUpdateFlags.html) flags =
MeshUpdateFlags.Default);

## Declaration

public void SetUVs(int channel, List<Vector3> uvs, int start, int length,
[Rendering.MeshUpdateFlags](Rendering.MeshUpdateFlags.html) flags =
MeshUpdateFlags.Default);

## Declaration

public void SetUVs(int channel, List<Vector4> uvs, int start, int length,
[Rendering.MeshUpdateFlags](Rendering.MeshUpdateFlags.html) flags =
MeshUpdateFlags.Default);

## Declaration

public void SetUVs(int channel, NativeArray<T> uvs, int start, int length,
[Rendering.MeshUpdateFlags](Rendering.MeshUpdateFlags.html) flags =
MeshUpdateFlags.Default);

### Parameters

channel | The UV channel, in [0..7] range.  
---|---  
uvs | UVs to set for the given index.  
start | Index of the first element to take from the input array.  
length | Number of elements to take from the input array.  
flags | Flags controlling the function behavior, see [MeshUpdateFlags](Rendering.MeshUpdateFlags.html).  
  
### Description

Sets the UVs of the Mesh, using a part of the input array.

This method behaves as if you called SetUVs with an array that is a slice of
the whole array, starting at `start` index and being of a given `length`. The
resulting Mesh has `length` amount of vertices.

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

