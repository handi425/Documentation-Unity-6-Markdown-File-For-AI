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

#  [GameObjectUtility](GameObjectUtility.html).DuplicateGameObject

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

public static [GameObject](GameObject.html)
DuplicateGameObject([GameObject](GameObject.html) gameObject);

### Parameters

gameObject | The GameObject to be duplicated.  
---|---  
  
### Returns

**GameObject** The duplicated GameObject.

### Description

Duplicates a single GameObject and returns the new GameObject.

Duplicates a GameObject within a Scene. The duplicated GameObject will be on
the same level in the hierarchy as the original GameObject, and they will
share the same parent. If there are any children or components that belong to
the original GameObject, the duplicate will have them as well.  
  
For duplicating more than one GameObject use
[DuplicateGameObjects](GameObjectUtility.DuplicateGameObjects.html). For
duplicating Assets use [CopyAsset](GameObjectUtility.CopyAsset.html).

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public static class DuplicateGameObjectExample
    {
        // Create context menu
        [[MenuItem](MenuItem.html)("Example/DuplicateGameObject")]
        public static void DuplicateTest()
        {
            // The original [GameObject](GameObject.html)
            [GameObject](GameObject.html) gameObject = new [GameObject](GameObject.html)();  
      
            // The duplicated [GameObject](GameObject.html)
            [GameObject](GameObject.html) duplicatedGameObject = [GameObjectUtility.DuplicateGameObject](GameObjectUtility.DuplicateGameObject.html)(gameObject);  
      
            // [Display](Display.html) the names of the original and duplicated GameObjects in the console
            [Debug.Log](Debug.Log.html)("The original [GameObject](GameObject.html): " + gameObject.name);
            [Debug.Log](Debug.Log.html)("The duplicated [GameObject](GameObject.html): " + duplicatedGameObject.name);
        }
    }
    

Any errors and warnings from the duplication operation are reported in the log
and the console.

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

