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

#  [Caching](Caching.html).ClearAllCachedVersions

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

public static bool ClearAllCachedVersions(string assetBundleName);

### Parameters

assetBundleName | The AssetBundle name.  
---|---  
  
### Returns

**bool** Returns true when cache clearing succeeded.

### Description

Removes all the cached versions of the given AssetBundle from the cache.

Returns false if any cached bundle is in use.

    
    
    using System.Collections;
    using UnityEngine.Networking;
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        IEnumerator ClearAllCachedVersionsExample(string uri)
        {
            //Download the bundle
            [UnityWebRequest](Networking.UnityWebRequest.html) request = [UnityWebRequestAssetBundle.GetAssetBundle](Networking.UnityWebRequestAssetBundle.GetAssetBundle.html)(uri);
            yield return request.SendWebRequest();
            [AssetBundle](AssetBundle.html) bundle = [DownloadHandlerAssetBundle.GetContent](Networking.DownloadHandlerAssetBundle.GetContent.html)(request);  
      
            //Given the name of an asset bundle, this will clear every cached version across all caches
            [Caching.ClearAllCachedVersions](Caching.ClearAllCachedVersions.html)(bundle.name);  
      
            //Unload the [AssetBundle](AssetBundle.html)
            bundle.Unload(true);
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

