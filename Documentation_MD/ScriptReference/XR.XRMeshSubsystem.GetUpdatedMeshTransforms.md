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

#  [XRMeshSubsystem](XR.XRMeshSubsystem.html).GetUpdatedMeshTransforms

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

public NativeArray<MeshTransform>
GetUpdatedMeshTransforms([Unity.Collections.Allocator](Unity.Collections.Allocator.html)
allocator);

### Parameters

allocator | The allocator to use for the returned NativeArray.  
---|---  
  
### Returns

**NativeArray <MeshTransform>** A new NativeArray of
[MeshTransform](XR.MeshTransform.html)s.

### Description

Gets the updated mesh transforms.

Use this to get updated transforms for each mesh tracked by the subsystem. The
number of transforms returned may be less than the total number of tracked
meshes. The results may be affected by previous calls to this method. That is,
only transforms that have changed since the last call to this method may be
returned.  
  
Typically, you should call this at regular intervals, for example, once per
frame, in order to update the transform of each mesh. When a mesh is generated
using
[XRMeshSubsystem.GenerateMeshAsync](XR.XRMeshSubsystem.GenerateMeshAsync.html),
the [MeshGenerationResult](XR.MeshGenerationResult.html) also contains a
transform and timestamp. Because generation is asynchronous, you can compare
timestamps to ensure you are using the most recent transform. Larger values
indicate newer transforms.  
  
This method always returns a new NativeArray, even when there are no updated
transforms. The caller is responsible for disposing the returned NativeArray.  
  
Additional resources: [MeshTransform](XR.MeshTransform.html),
[XRMeshSubsystem.GenerateMeshAsync](XR.XRMeshSubsystem.GenerateMeshAsync.html),
[MeshGenerationResult](XR.MeshGenerationResult.html)

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

