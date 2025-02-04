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

**Method group is Obsolete**  

# PreferenceItem

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

**Obsolete** [PreferenceItem] is deprecated. Use [SettingsProvider] instead.

### Description

(Obsolete: use the SettingsProvider class instead) The PreferenceItem
attribute allows you to add preferences sections to the Preferences window.

The PreferenceItem attribute turns any static function into an OnGUI callback.
Only static functions can use the PreferenceItem attribute. By default all
current PreferenceItems are included in the Unified Settings window and you
get a warning to use the SettingsProvider attribute instead.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        // Have we loaded the prefs yet
        private static bool prefsLoaded = false;  
      
        // The Preferences
        public static bool boolPreference = false;  
      
        // Add preferences section named "My Preferences" to the Preferences window
        [PreferenceItem("My Preferences")]
        public static void PreferencesGUI()
        {
            // Load the preferences
            if (!prefsLoaded)
            {
                boolPreference = [EditorPrefs.GetBool](EditorPrefs.GetBool.html)("BoolPreferenceKey", false);
                prefsLoaded = true;
            }  
      
            // Preferences [GUI](GUI.html)
            boolPreference = [EditorGUILayout.Toggle](EditorGUILayout.Toggle.html)("Bool Preference", boolPreference);  
      
            // Save the preferences
            if ([GUI.changed](GUI-changed.html))
                [EditorPrefs.SetBool](EditorPrefs.SetBool.html)("BoolPreferenceKey", boolPreference);
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

