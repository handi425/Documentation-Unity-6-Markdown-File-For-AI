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

#
[ModelImporterClipAnimation](ModelImporterClipAnimation.html).ConfigureMaskFromClip

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

public void ConfigureMaskFromClip(ref [AvatarMask](AvatarMask.html) mask);

### Parameters

mask |  [AvatarMask](AvatarMask.html) to which the masking values will be saved.  
---|---  
  
### Description

Copy the current masking settings from the clip to an
[AvatarMask](AvatarMask.html).

When writing an [AssetPostprocessor](AssetPostprocessor.html), use this method
to copy the [AvatarMask](AvatarMask.html) from your clip configuration so that
you can modify it.  
  
Note: you will need to use
[ModelImporterClipAnimation.ConfigureClipFromMask](ModelImporterClipAnimation.ConfigureClipFromMask.html)
to apply the [AvatarMask](AvatarMask.html) back on the
[ModelImporterClipAnimation](ModelImporterClipAnimation.html)  
  
See also:
[ModelImporterClipAnimation.ConfigureClipFromMask](ModelImporterClipAnimation.ConfigureClipFromMask.html).

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class CopyAvatarMask : [AssetPostprocessor](AssetPostprocessor.html)
    {
        void OnPreprocessAnimation()
        {
            var modelImporter = assetImporter as [ModelImporter](ModelImporter.html);  
      
            //Create a new [AvatarMask](AvatarMask.html) to edit the mask
            var mask = new [AvatarMask](AvatarMask.html)();
            var clips = modelImporter.clipAnimations;  
      
            //Acquire the mask from the clip
            clips[0].ConfigureMaskFromClip(ref mask);  
      
            //Filter out the first non-root (0) bone
            mask.SetTransformActive(1, false);  
      
            //Apply the mask back to the clip
            clips[0].ConfigureClipFromMask(mask);  
      
            //Apply the clips back to the [ModelImporter](ModelImporter.html)
            modelImporter.clipAnimations = clips;  
      
            //Destroy the [AvatarMask](AvatarMask.html) since we're not using it anymore
            [Object.DestroyImmediate](Object.DestroyImmediate.html)(mask);
        }
    }
    

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

