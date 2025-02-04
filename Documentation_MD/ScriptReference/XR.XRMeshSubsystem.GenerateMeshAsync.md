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

#  [XRMeshSubsystem](XR.XRMeshSubsystem.html).GenerateMeshAsync

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

## Declaration

public void GenerateMeshAsync([XR.MeshId](XR.MeshId.html) meshId,
[Mesh](Mesh.html) mesh, [MeshCollider](MeshCollider.html) meshCollider,
[XR.MeshVertexAttributes](XR.MeshVertexAttributes.html) attributes,
Action<MeshGenerationResult> onMeshGenerationComplete);

### Parameters

meshId | The [MeshId](XR.MeshId.html) of the mesh you wish to generate.  
---|---  
mesh | The [Mesh](Mesh.html) to write the results into.  
meshCollider | (Optional) The [MeshCollider](MeshCollider.html) to populate with physics data. This may be null.  
attributes | The vertex attributes you'd like to use.  
onMeshGenerationComplete | The delegate to invoke when the generation completes.  
  
### Description

Requests the generation of the Mesh with [MeshId](XR.MeshId.html) `meshId`.
Unity calls `onMeshGenerationComplete` when generation finishes.

Use this method to request that a mesh is asynchronously generated.
"Generation" includes extracting the mesh data from the subsystem's mesh
provider (e.g., an AR device) and baking the [MeshCollider](MeshCollider.html)
(if `meshCollider` is not null).  
  
This happens in a background thread. For large meshes, this can take several
frames to complete. `onMeshGenerationComplete` is invoked when the generation
completes.  
  
The mesh vertices are provided in session space.  
  
Additional resources:
[XRMeshSubsystem.TryGetMeshInfos](XR.XRMeshSubsystem.TryGetMeshInfos.html)

* * *

## Declaration

public void GenerateMeshAsync([XR.MeshId](XR.MeshId.html) meshId,
[Mesh](Mesh.html) mesh, [MeshCollider](MeshCollider.html) meshCollider,
[XR.MeshVertexAttributes](XR.MeshVertexAttributes.html) attributes,
Action<MeshGenerationResult> onMeshGenerationComplete,
[XR.MeshGenerationOptions](XR.MeshGenerationOptions.html) options);

### Parameters

meshId | The [MeshId](XR.MeshId.html) of the mesh you wish to generate.  
---|---  
mesh | The [Mesh](Mesh.html) to write the results into.  
meshCollider | (Optional) The [MeshCollider](MeshCollider.html) to populate with physics data. This may be null.  
attributes | The vertex attributes you'd like to use.  
onMeshGenerationComplete | The delegate to invoke when the generation completes.  
options | The mesh generation options.  
  
### Description

Requests the generation of the Mesh with [MeshId](XR.MeshId.html) `meshId`.
Unity calls `onMeshGenerationComplete` when generation finishes.

This variant allows you to specify additional mesh generation options.  
  
**Note:** If the
[MeshGenerationOptions.ConsumeTransform](XR.MeshGenerationOptions.ConsumeTransform.html)
flag is set in the `options` argument, the resulting mesh will be relative to
the transform provided by the
[MeshGenerationResult](XR.MeshGenerationResult.html). If this flag is not set,
the vertices are transformed into session space and the
[MeshGenerationResult](XR.MeshGenerationResult.html) will contain an identity
transform.  
  
Additional resources:
[XRMeshSubsystem.TryGetMeshInfos](XR.XRMeshSubsystem.TryGetMeshInfos.html)

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

