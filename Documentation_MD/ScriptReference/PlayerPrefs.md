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

# PlayerPrefs

class in UnityEngine

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

`PlayerPrefs` is a class that stores Player preferences between game sessions.
It can store string, float and integer values into the user’s platform
registry.

Unity stores PlayerPrefs in a local registry, without encryption. Do not use
PlayerPrefs data to store sensitive data.  
  
Unity stores `PlayerPrefs` data differently based on which operating system
the application runs on. In the file paths given on this page, the
ExampleCompanyName and ExampleProductName are the names you set in Unity’s
[Player Settings](../Manual/class-PlayerSettings.html).  
  
  
  
**Standalone player and in-Editor Play mode storage location**  
  
\- **MacOS** :
`~/Library/Preferences/com.ExampleCompanyName.ExampleProductName.plist`  
  
**Standalone Player storage location**  
  
\- **Android** : `/data/data/pkg-name/shared_prefs/pkg-
name.v2.playerprefs.xml`.  
  
**Notes** :

  * Unity uses [SharedPreferences](https://developer.android.com/reference/android/content/SharedPreferences) API to access the `PlayerPrefs` data and [SharedPreferences.Editor](https://developer.android.com/reference/android/content/SharedPreferences.Editor) API to modify it.
  * C#, Android Java, and native code can all access the `PlayerPrefs` data.

\- **iOS** : Uses the `[NSUserDefaults standardUserDefaults]` API to store
PlayerPrefs data.  
  
\- **Linux** : `~/.config/unity3d/ExampleCompanyName/ExampleProductName`  
  
\- **WebGL** : Unity stores up to 1MB of PlayerPrefs data using the browser's
IndexedDB API. For more information, see
[IndexedDB](https://developers.google.com/web/ilt/pwa/lab-indexeddb#overview).  
  
\- **Windows** : `HKCU\Software\ExampleCompanyName\ExampleProductName`  
  
\- **Windows Universal Platform** :
`%userprofile%\AppData\Local\Packages\[ProductPackageId]\LocalState\playerprefs.dat`  
  
  
  
**In-Editor Play mode storage location**  
  
\- **Windows** :
`HKCU\Software\Unity\UnityEditor\ExampleCompanyName\ExampleProductName` key.
Note that Windows uses the key names from the application’s PlayerPrefs as a
hashed identifier. For example, Unity adds a `DeckBase` string to the hashed
key name (for example `h3232628825`) to create `DeckBase_h3232628825`. Unity
hashes the names because it:

  * Allows Unity to store case-sensitive key names.
  * Prevents naming conflicts with data the application stores outside of PlayerPrefs.
  * Ensures that you use the PlayerPrefs API to access and modify the values.

The application ignores the extension.

### Static Methods

[DeleteAll](PlayerPrefs.DeleteAll.html)| Removes all keys and values from the
preferences. Use with caution.  
---|---  
[DeleteKey](PlayerPrefs.DeleteKey.html)| Removes the given key from the
PlayerPrefs. If the key does not exist, DeleteKey has no impact.  
[GetFloat](PlayerPrefs.GetFloat.html)| Returns the value corresponding to key
in the preference file if it exists.  
[GetInt](PlayerPrefs.GetInt.html)| Returns the value corresponding to key in
the preference file if it exists.  
[GetString](PlayerPrefs.GetString.html)| Returns the value corresponding to
key in the preference file if it exists.  
[HasKey](PlayerPrefs.HasKey.html)| Returns true if the given key exists in
PlayerPrefs, otherwise returns false.  
[Save](PlayerPrefs.Save.html)| Saves all modified preferences.  
[SetFloat](PlayerPrefs.SetFloat.html)| Sets the float value of the preference
identified by the given key. You can use PlayerPrefs.GetFloat to retrieve this
value.  
[SetInt](PlayerPrefs.SetInt.html)| Sets a single integer value for the
preference identified by the given key. You can use PlayerPrefs.GetInt to
retrieve this value.  
[SetString](PlayerPrefs.SetString.html)| Sets a single string value for the
preference identified by the given key. You can use PlayerPrefs.GetString to
retrieve this value.  
  
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

