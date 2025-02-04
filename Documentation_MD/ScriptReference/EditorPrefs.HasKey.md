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

#  [EditorPrefs](EditorPrefs.html).HasKey

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

public static bool HasKey(string key);

### Parameters

key | Name of key to check for.  
---|---  
  
### Returns

**bool** The existence or not of the key.

### Description

Returns true if `key` exists in the preferences file.

The preferences file is examined to identify whether the specified key exists.
True or false is returned. In the following example a key and value can be
written into the preference file, or deleted. The existence of the key is
checked with the [HasKey](EditorPrefs.HasKey.html) function and a message
displayed.  
  
![](../StaticFiles/ScriptRefImages/EditorPrefsHasKey.png)  
_Use save, delete, and HasKey preference check._

    
    
    // Small example where the XyZ key can be saved or deleted from the Preferences file.
    // The existence of the key is checked using the HasKey() function.  
      
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class HasKeyExample : [EditorWindow](EditorWindow.html)
    {
        private string keyName = "XyZ";  
      
        [[MenuItem](MenuItem.html)("Examples/HasKey Example")]
        static void Init()
        {
            HasKeyExample window = (HasKeyExample)[EditorWindow.GetWindowWithRect](EditorWindow.GetWindowWithRect.html)(
                typeof(HasKeyExample), new [Rect](Rect.html)(0, 0, 250, 80));
            window.Show();
        }  
      
        void OnGUI()
        {
            [EditorGUILayout.BeginHorizontal](EditorGUILayout.BeginHorizontal.html)();  
      
            if ([GUILayout.Button](GUILayout.Button.html)("Save '" + keyName + "' as Key"))
                [EditorPrefs.SetString](EditorPrefs.SetString.html)(keyName, "abc123");  
      
            if ([GUILayout.Button](GUILayout.Button.html)("Delete Key '" + keyName + "'"))
                [EditorPrefs.DeleteKey](EditorPrefs.DeleteKey.html)(keyName);  
      
            [EditorGUILayout.EndHorizontal](EditorGUILayout.EndHorizontal.html)();  
      
            [GUILayout.Label](GUILayout.Label.html)(keyName + " key exists: " + [EditorPrefs.HasKey](EditorPrefs.HasKey.html)(keyName));  
      
            if ([GUILayout.Button](GUILayout.Button.html)("Close"))
                this.Close();
        }  
      
        // delete the key each time the demo starts
        void OnFocus()
        {
            [EditorPrefs.DeleteKey](EditorPrefs.DeleteKey.html)(keyName);
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

