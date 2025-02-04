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

# EditorPrefs

class in UnityEditor

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

Stores and accesses Unity Editor preferences.

On macOS, EditorPrefs are stored in
`~/Library/Preferences/com.unity3d.UnityEditor5.x.plist`.  
  
On Windows, EditorPrefs are stored in the registry under the
`HKCU\Software\Unity Technologies\Unity Editor 5.x` key.  
  
On Linux, EditorPrefs are stored in `~/.local/share/unity3d/prefs`.

### Static Methods

[DeleteAll](EditorPrefs.DeleteAll.html)| Removes all keys and values from the
preferences. Use with caution.  
---|---  
[DeleteKey](EditorPrefs.DeleteKey.html)| Removes key and its corresponding
value from the preferences.  
[GetBool](EditorPrefs.GetBool.html)| Returns the value corresponding to key in
the preference file if it exists.  
[GetFloat](EditorPrefs.GetFloat.html)| Returns the float value corresponding
to key if it exists in the preference file.  
[GetInt](EditorPrefs.GetInt.html)| Returns the value corresponding to key in
the preference file if it exists.  
[GetString](EditorPrefs.GetString.html)| Returns the value corresponding to
key in the preference file if it exists.  
[HasKey](EditorPrefs.HasKey.html)| Returns true if key exists in the
preferences file.  
[SetBool](EditorPrefs.SetBool.html)| Sets the value of the preference
identified by key.  
[SetFloat](EditorPrefs.SetFloat.html)| Sets the float value of the preference
identified by key.  
[SetInt](EditorPrefs.SetInt.html)| Sets the value of the preference identified
by key as an integer.  
[SetString](EditorPrefs.SetString.html)| Sets the value of the preference
identified by key. Note that EditorPrefs does not support null strings and
will store an empty string instead.  
  
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

