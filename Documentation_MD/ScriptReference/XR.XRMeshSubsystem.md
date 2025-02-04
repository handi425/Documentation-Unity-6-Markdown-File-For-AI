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

# XRMeshSubsystem

class in UnityEngine.XR

/

Inherits from:[IntegratedSubsystem](IntegratedSubsystem.html)

/

Implemented in:[UnityEngine.XRModule](UnityEngine.XRModule.html)

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

Allows external systems to provide dynamic meshes to Unity.

The XRMeshSubsystem enables external systems to provide dynamic meshes to
Unity. The meshes are processed on background threads, including physics
baking, so as not to block the main thread during execution. This is useful
for that provide dynamic meshes during runtime, such as spatially-aware AR
devices.

### Properties

[meshDensity](XR.XRMeshSubsystem-meshDensity.html)| Call this function to
request a change in the density of the generated Meshes. Unity gives the
density level as a value within the range 0.0 to 1.0 and the provider
determines how to map that value to their implementation. Setting this value
does not guarantee an immediate change in the density of any currently created
Mesh and may only change the density for new or updated Meshes.  
---|---  
  
### Public Methods

[GenerateMeshAsync](XR.XRMeshSubsystem.GenerateMeshAsync.html)| Requests the
generation of the Mesh with MeshId meshId. Unity calls
onMeshGenerationComplete when generation finishes.  
---|---  
[GetUpdatedMeshTransforms](XR.XRMeshSubsystem.GetUpdatedMeshTransforms.html)|
Gets the updated mesh transforms.  
[SetBoundingVolume](XR.XRMeshSubsystem.SetBoundingVolume.html)| Set the
bounding volume to restrict the space in which Unity generates and tracks
Meshes.The bounding volume is an Axis Aligned Bounding Box (AABB) centered at
the origin and extends in each dimension as defined in extents.The units of
measurement depend on the provider.  
[TryGetMeshInfos](XR.XRMeshSubsystem.TryGetMeshInfos.html)| Gets information
about every Mesh the system currently tracks.  
  
### Inherited Members

### Properties

[running](IntegratedSubsystem-running.html)| Whether or not the subsystem is
running.  
---|---  
  
### Public Methods

[Destroy](IntegratedSubsystem.Destroy.html)| Destroys this instance of a
subsystem.  
---|---  
[Start](IntegratedSubsystem.Start.html)| Starts an instance of a subsystem.  
[Stop](IntegratedSubsystem.Stop.html)| Stops an instance of a subsystem.  
  
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

