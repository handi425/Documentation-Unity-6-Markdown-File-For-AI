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

#  [Caching](Caching.html).RemoveCache

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

public static bool RemoveCache([Cache](Cache.html) cache);

### Parameters

cache | The Cache to be removed.  
---|---  
  
### Returns

**bool** Returns true if the Cache is removed.

### Description

Removes the Cache from cache list.

    
    
    using System.IO;
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void RemoveCacheExample()
        {
            [Directory.CreateDirectory](Windows.Directory.CreateDirectory.html)("Cache1");
            [Directory.CreateDirectory](Windows.Directory.CreateDirectory.html)("Cache2");
            [Directory.CreateDirectory](Windows.Directory.CreateDirectory.html)("Cache3");  
      
            [Cache](Cache.html) c1 = [Caching.AddCache](Caching.AddCache.html)("Cache1"); //Placed in cache list at position 1
            [Cache](Cache.html) c2 = [Caching.AddCache](Caching.AddCache.html)("Cache2"); //Placed in cache list at position 2
            [Cache](Cache.html) c3 = [Caching.AddCache](Caching.AddCache.html)("Cache3"); //Placed in cache list at position 3  
      
            bool successfullyRemovedCache = [Caching.RemoveCache](Caching.RemoveCache.html)(c1);  
      
            if (!successfullyRemovedCache)
            {
                [Debug.Log](Debug.Log.html)("Unable to remove cache.");
            }  
      
            //Now, if the remove was successful, the [Cache](Cache.html) list looks like:
            //[Position](UIElements.Position.html) 0: Default [Cache](Cache.html)
            //[Position](UIElements.Position.html) 1: Cache2
            //[Position](UIElements.Position.html) 2: Cache3
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

