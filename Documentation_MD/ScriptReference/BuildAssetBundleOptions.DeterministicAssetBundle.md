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

**Method group is Obsolete**  

#
[BuildAssetBundleOptions](BuildAssetBundleOptions.html).DeterministicAssetBundle

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

**Obsolete** This has been made obsolete. It is always enabled in the new
AssetBundle build system introduced in 5.0.

### Description

Builds an asset bundle using a hash for the id of the object stored in the
asset bundle.

This allows you to rebuild an asset bundle and reference assets in it
directly. When rebuilding the asset bundle the objects in it are guaranteed to
have the same id after rebuilding the asset bundle. Due to it being a 32 bit
hash space, if you have a lot of objects in the asset bundle it will increase
the potential for hash conflicts. Unity will give an error and not build the
asset bundle in that case. The hash is based on the GUID of the asset and the
local id of the object in the asset. DeterministicAssetBundle are also slower
to load from than normal asset bundles, this is because the threaded
background loading API usually expects objects to be ordered in a way that
makes reading reduce seeking. With DeterministicAssetBundles that is not
possible.  
  
This flag is only taken into account when calling the obsolete
BuildPipeline.BuildAssetBundle method. When calling
[BuildPipeline.BuildAssetBundles](BuildPipeline.BuildAssetBundles.html) this
behaviour is always enabled.

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

