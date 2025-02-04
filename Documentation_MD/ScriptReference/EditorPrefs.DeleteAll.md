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

#  [EditorPrefs](EditorPrefs.html).DeleteAll

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

public static void DeleteAll();

### Description

Removes all keys and values from the preferences. Use with caution.

![](../StaticFiles/ScriptRefImages/ClearEditorPrefs.png)  
_Clears all editor prefs keys._

    
    
    // Clear all the editor prefs keys.
    //
    // Warning: this will also remove editor preferences as the opened projects, etc.  
      
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class DeleteAllExample : [ScriptableObject](ScriptableObject.html)
    {
        [[MenuItem](MenuItem.html)("Examples/[EditorPrefs](EditorPrefs.html)/Clear all [Editor](Editor.html) Preferences")]
        static void deleteAllExample()
        {
            if ([EditorUtility.DisplayDialog](EditorUtility.DisplayDialog.html)("Delete all editor preferences.",
                "Are you sure you want to delete all the editor preferences? " +
                "This action cannot be undone.", "Yes", "No"))
            {
                [Debug.Log](Debug.Log.html)("yes");
                [EditorPrefs.DeleteAll](EditorPrefs.DeleteAll.html)();
            }
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

