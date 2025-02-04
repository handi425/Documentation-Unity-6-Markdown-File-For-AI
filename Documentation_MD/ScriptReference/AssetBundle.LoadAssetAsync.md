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

#  [AssetBundle](AssetBundle.html).LoadAssetAsync

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

public [AssetBundleRequest](AssetBundleRequest.html) LoadAssetAsync(string
name);

## Declaration

public [AssetBundleRequest](AssetBundleRequest.html) LoadAssetAsync(string
name);

## Declaration

public [AssetBundleRequest](AssetBundleRequest.html) LoadAssetAsync(string
name, Type type);

### Parameters

name | Name of the Asset. For the most precise matching this should be the relative path of the Asset that was built into the AssetBundle, including the file extension. The relative path and file extension are optional, and Assets can be found and loaded based on the filename alone. However this opens the potential for unexpected results if the filename is not unique within the AssetBundle. At build time it is also possible to specify a name for the Asset using [AssetBundleBuild.addressableNames](AssetBundleBuild-addressableNames.html). In that case that specified name will be expected to load the Asset instead of the Asset path.   
---|---  
type | The provided type will be checked against the Asset's main object, and if that is not compatible it will be matched against visible objects within the Asset. Not all nested objects are visible, for example this will not work to directly retrieve a Transform, MonoBehaviour or other Component. In cases where there are multiple matches for the name argument, the requested type can determine which Asset to load.  
  
### Description

Asynchronously loads an Asset from the bundle.

The LoadAssetAsync<T> signature is recommended, so that the requested type is
explicit and no type casting is necessary.  
  
Note: For Scenes inside AssetBundles call
[SceneManager.LoadSceneAsync](SceneManagement.SceneManager.LoadSceneAsync.html)
instead of this method.  
  
Additional resources: [AssetBundleRequest](AssetBundleRequest.html).

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

