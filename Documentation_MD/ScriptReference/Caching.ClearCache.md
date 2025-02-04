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

#  [Caching](Caching.html).ClearCache

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

public static bool ClearCache();

## Declaration

public static bool ClearCache(int expiration);

### Parameters

expiration | The number of seconds that AssetBundles may remain unused in the cache.  
---|---  
  
### Returns

**bool** True when cache clearing succeeded, false if cache was in use.

### Description

Removes all AssetBundle content that has been cached by the current
application.

This method is not available to WebPlayer applications that use the shared
cache.  
  
Additional resources: [Downloading Asset Bundles](../Manual/UnityWebRequest-
DownloadingAssetBundle.html).

    
    
    using System.IO;
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void ClearCacheExample()
        {
            [Directory.CreateDirectory](Windows.Directory.CreateDirectory.html)("Cache1");
            [Directory.CreateDirectory](Windows.Directory.CreateDirectory.html)("Cache2");
            [Directory.CreateDirectory](Windows.Directory.CreateDirectory.html)("Cache3");  
      
            [Caching.AddCache](Caching.AddCache.html)("Cache1"); //Placed in cache list at position 1
            [Caching.AddCache](Caching.AddCache.html)("Cache2"); //Placed in cache list at position 2
            [Caching.AddCache](Caching.AddCache.html)("Cache3"); //Placed in cache list at position 3  
      
            //Clears all of the caches
            bool success = [Caching.ClearCache](Caching.ClearCache.html)();  
      
            if (!success)
            {
                [Debug.Log](Debug.Log.html)("Unable to clear cache");
            }
        }
    }
    

Web player is not supported from 5.4.0 and beyond.

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

