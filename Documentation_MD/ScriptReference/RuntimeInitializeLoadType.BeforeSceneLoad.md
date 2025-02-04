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

#  [RuntimeInitializeLoadType](RuntimeInitializeLoadType.html).BeforeSceneLoad

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

Callback invoked when the first scene's objects are loaded into memory but
**before** Awake has been called.

For more info on ordering see
[RuntimeInitializeOnLoadMethodAttribute](RuntimeInitializeOnLoadMethodAttribute.html).

    
    
    // Demonstration of the [RuntimeInitializeLoadType.BeforeSceneLoad](RuntimeInitializeLoadType.BeforeSceneLoad.html) attribute to find inactive objects before Awake has been 
    // called for the first scene being loaded. Then from these inactive objects we find which ones will be active after Awake is called later.
    using UnityEngine;  
      
    class MyClass
    {
        [RuntimeInitializeOnLoadMethod([RuntimeInitializeLoadType.BeforeSceneLoad](RuntimeInitializeLoadType.BeforeSceneLoad.html))]
        private static void FirstSceneLoading()
        {
            var components = UnityEngine.Object.FindObjectsByType(typeof([MonoBehaviour](MonoBehaviour.html)), [FindObjectsInactive.Include](FindObjectsInactive.Include.html), [FindObjectsSortMode.None](FindObjectsSortMode.None.html));
            var willBeActiveAfterSceneLoad = 0;
            foreach (var c in components)
            {
                if (WillBeActiveAfterSceneLoad((([Component](Component.html))c).gameObject))
                    willBeActiveAfterSceneLoad++;
            }
            [Debug.Log](Debug.Log.html)("BeforeSceneLoad. Will be Active after Awake, count: " + willBeActiveAfterSceneLoad);
        }  
      
        static bool WillBeActiveAfterSceneLoad([GameObject](GameObject.html) gameObject)
        {
            [Transform](Transform.html) current = gameObject.transform;
            while (current != null)
            {
                if (!current.gameObject.activeSelf)
                    return false;  
      
                current = current.parent;
            }  
      
            return true;
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

