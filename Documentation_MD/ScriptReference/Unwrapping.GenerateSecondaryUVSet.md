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

#  [Unwrapping](Unwrapping.html).GenerateSecondaryUVSet

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

public static bool GenerateSecondaryUVSet([Mesh](Mesh.html) src);

## Declaration

public static bool GenerateSecondaryUVSet([Mesh](Mesh.html) src,
[UnwrapParam](UnwrapParam.html) settings);

### Parameters

src | The Mesh to update.  
---|---  
settings | Settings that configure the calculation.  
  
### Returns

**bool** Returns true if the calculation succeeded. Otherwise, returns false.

### Description

Compute a unique UV layout for a Mesh, and store it in [Mesh.uv2](Mesh-
uv2.html).

When you import a model asset, you can instruct Unity to compute a lightmap UV
layout for it using [[ModelImporter-generateSecondaryUV]] or the [Model Import
Settings Inspector](../Manual/class-FBXImporter.html). This function allows
you to do the same to procedurally generated meshes.  
  
If this process requires multiple UV charts to flatten the the mesh, the mesh
might contain more vertices than before. If the mesh uses 16-bit indices (see
[Mesh.indexFormat](Mesh-indexFormat.html)) and the process would result in
more vertices than are possible to use with 16-bit indices, this function
fails and returns `false`.  
  
Additional resources: [Mesh](Mesh.html) class,
[ModelImporter](ModelImporter.html) class, [Generating Lightmap
UVs](../Manual/LightingGiUvs-GeneratingLightmappingUVs.html).

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

