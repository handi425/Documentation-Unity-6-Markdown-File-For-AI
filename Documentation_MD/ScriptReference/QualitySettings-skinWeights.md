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

#  [QualitySettings](QualitySettings.html).skinWeights

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

[Switch to Manual](../Manual/class-QualitySettings.html "Go to QualitySettings
Component in the Manual")

public static [SkinWeights](SkinWeights.html) skinWeights;

### Description

The maximum number of bones per vertex that are taken into account during
skinning, for all meshes in the project.

The value can be either One Bone, Two Bones, Four Bones or Auto. Note that
higher bone counts may have a performance cost, especially above 4 bones per
vertex.  
  
This setting does not change the underlying mesh data; it only affects the
number of bone weights that Unity uses when performing skinning. This means
that a mesh can have bone weight data that is unused due to this setting. You
can change this value at runtime.  
  
You can set this value for a single mesh using
[SkinnedMeshRenderer.quality](SkinnedMeshRenderer-quality.html). You can set
the maximum number of bone weights that mesh data stores for a single vertex
using [ModelImporter.maxBonesPerVertex](ModelImporter-maxBonesPerVertex.html).

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Set skin weights to one bone for all Meshes
            [QualitySettings.skinWeights](QualitySettings-skinWeights.html) = [SkinWeights.OneBone](SkinWeights.OneBone.html);
        }
    }
    

Additional resources: [ModelImporter.maxBonesPerVertex](ModelImporter-
maxBonesPerVertex.html), [ModelImporter.minBoneWeight](ModelImporter-
minBoneWeight.html), [ModelImporter.skinWeights](ModelImporter-
skinWeights.html), [SkinnedMeshRenderer.quality](SkinnedMeshRenderer-
quality.html), [BoneWeight](BoneWeight.html), [BoneWeight1](BoneWeight1.html).

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

