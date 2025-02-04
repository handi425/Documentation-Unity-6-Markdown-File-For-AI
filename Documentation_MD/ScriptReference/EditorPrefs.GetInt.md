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

#  [EditorPrefs](EditorPrefs.html).GetInt

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

public static int GetInt(string key);

## Declaration

public static int GetInt(string key, int defaultValue = 0);

### Parameters

key | Name of key to read integer from.  
---|---  
defaultValue | Integer value to return if the key is not in the storage.  
  
### Returns

**int** The value stored in the preference file.

### Description

Returns the value corresponding to `key` in the preference file if it exists.

If the value doesn't already exist in the preference file the function will
return `defaultValue`.  
  
Additional resources: [SetInt](EditorPrefs.SetInt.html).

    
    
    // A small editor window that allows an integer value to be
    // read and written to the [EditorPrefs](EditorPrefs.html) online storage.
    //
    // SetIntExample is the name of the int to read/write.  
      
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class ExampleClass : [EditorWindow](EditorWindow.html)
    {
        int intValue = 42;  
      
        [[MenuItem](MenuItem.html)("Examples/Prefs.GetInt Example")]
        static void Init()
        {
            ExampleClass window = (ExampleClass)[EditorWindow.GetWindow](EditorWindow.GetWindow.html)(typeof(ExampleClass));
            window.Show();
        }  
      
        void OnGUI()
        {
            int temp;
            temp = [EditorPrefs.GetInt](EditorPrefs.GetInt.html)("SetIntExample", -1);
            [EditorGUILayout.LabelField](EditorGUILayout.LabelField.html)("Current stored value: " + temp.ToString());
            intValue = [EditorGUILayout.IntField](EditorGUILayout.IntField.html)("Value to write to Prefs: ", intValue);
            if ([GUILayout.Button](GUILayout.Button.html)("Save value: " + intValue.ToString()))
            {
                [EditorPrefs.SetInt](EditorPrefs.SetInt.html)("SetIntExample", intValue);
                [Debug.Log](Debug.Log.html)("SetInt: " + intValue);
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

