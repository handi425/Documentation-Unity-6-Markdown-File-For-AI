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

#  [AssetBundle](AssetBundle.html).Unload

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

public void Unload(bool unloadAllLoadedObjects);

### Parameters

unloadAllLoadedObjects | Determines whether the current instances of objects loaded from the AssetBundle will also be unloaded.  
---|---  
  
### Description

Unloads an AssetBundle freeing its data.

When `unloadAllLoadedObjects` is false, tracking data structures and any
memory buffers holding content of the AssetBundle will be freed. But any
instances of objects loaded from this bundle will remain intact.  
  
When `unloadAllLoadedObjects` is true, all objects that were loaded from this
bundle will be destroyed as well. If there are GameObjects in your Scene
referencing those assets, the references to them will become missing.  
  
In either case you won't be able to load any more objects from this bundle
unless it is reloaded.  
  
See [AssetBundles compression](../Manual/AssetBundles-Cache.html) for a
description of the different compression formats used and their impact on
memory while loaded.  
  
Additional resources:
[UnloadAllAssetBundles](AssetBundle.UnloadAllAssetBundles.html),
[UnloadAsync](AssetBundle.UnloadAsync.html), [Using AssetBundles
Natively](../Manual/AssetBundles-Native.html).

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

