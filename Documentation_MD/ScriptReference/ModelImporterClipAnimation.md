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

# ModelImporterClipAnimation

class in UnityEditor

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

Animation clips to split animation into.

### Properties

[additiveReferencePoseFrame](ModelImporterClipAnimation-
additiveReferencePoseFrame.html)| The additive reference pose frame.  
---|---  
[curves](ModelImporterClipAnimation-curves.html)| Additionnal curves that will
be that will be added during the import process.  
[cycleOffset](ModelImporterClipAnimation-cycleOffset.html)| Offset to the
cycle of a looping animation, if a different time in it is desired to be the
start.  
[events](ModelImporterClipAnimation-events.html)| AnimationEvents that will be
added during the import process.  
[firstFrame](ModelImporterClipAnimation-firstFrame.html)| First frame of the
clip.  
[hasAdditiveReferencePose](ModelImporterClipAnimation-
hasAdditiveReferencePose.html)| Enable to defines an additive reference pose.  
[heightFromFeet](ModelImporterClipAnimation-heightFromFeet.html)| Keeps the
feet aligned with the root transform position.  
[heightOffset](ModelImporterClipAnimation-heightOffset.html)| Offset to the
vertical root position.  
[keepOriginalOrientation](ModelImporterClipAnimation-
keepOriginalOrientation.html)| Keeps the vertical position as it is authored
in the source file.  
[keepOriginalPositionXZ](ModelImporterClipAnimation-
keepOriginalPositionXZ.html)| Keeps the vertical position as it is authored in
the source file.  
[keepOriginalPositionY](ModelImporterClipAnimation-
keepOriginalPositionY.html)| Keeps the vertical position as it is authored in
the source file.  
[lastFrame](ModelImporterClipAnimation-lastFrame.html)| Last frame of the
clip.  
[lockRootHeightY](ModelImporterClipAnimation-lockRootHeightY.html)| Enable to
make vertical root motion be baked into the movement of the bones. Disable to
make vertical root motion be stored as root motion.  
[lockRootPositionXZ](ModelImporterClipAnimation-lockRootPositionXZ.html)|
Enable to make horizontal root motion be baked into the movement of the bones.
Disable to make horizontal root motion be stored as root motion.  
[lockRootRotation](ModelImporterClipAnimation-lockRootRotation.html)| Enable
to make root rotation be baked into the movement of the bones. Disable to make
root rotation be stored as root motion.  
[loop](ModelImporterClipAnimation-loop.html)| Is the clip a looping animation?  
[loopPose](ModelImporterClipAnimation-loopPose.html)| Enable to make the
motion loop seamlessly.  
[loopTime](ModelImporterClipAnimation-loopTime.html)| Enable to make the clip
loop.  
[maskNeedsUpdating](ModelImporterClipAnimation-maskNeedsUpdating.html)|
Returns true when the source AvatarMask has changed. This only happens when
ModelImporterClipAnimation.maskType is set to
ClipAnimationMaskType.CopyFromOther To force a reload of the mask, simply set
ModelImporterClipAnimation.maskSource to the desired AvatarMask.  
[maskSource](ModelImporterClipAnimation-maskSource.html)| The AvatarMask used
to mask transforms during the import process.  
[maskType](ModelImporterClipAnimation-maskType.html)| Define mask type.  
[mirror](ModelImporterClipAnimation-mirror.html)| Mirror left and right in
this clip.  
[name](ModelImporterClipAnimation-name.html)| Clip name.  
[rotationOffset](ModelImporterClipAnimation-rotationOffset.html)| Offset in
degrees to the root rotation.  
[takeName](ModelImporterClipAnimation-takeName.html)| Take name.  
[wrapMode](ModelImporterClipAnimation-wrapMode.html)| The wrap mode of the
animation.  
  
### Public Methods

[ConfigureClipFromMask](ModelImporterClipAnimation.ConfigureClipFromMask.html)|
Copy the mask settings from an AvatarMask to the clip configuration.  
---|---  
[ConfigureMaskFromClip](ModelImporterClipAnimation.ConfigureMaskFromClip.html)|
Copy the current masking settings from the clip to an AvatarMask.  
  
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

