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

# IShortcutManager

interface in UnityEditor.ShortcutManagement

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

Represents a manager that configures a particular instance of the shortcuts
system.

The manager maintains a list of _available_ profiles which can be retrieved
with
[GetAvailableProfiles](ShortcutManagement.IShortcutManager.GetAvailableProfiles.html).
Some of the methods require the passed profile ID to be available at the time
it is called. Creating a new profile with
[CreateProfile](ShortcutManagement.IShortcutManager.CreateProfile.html) makes
it available and deleting a profile with
[DeleteProfile](ShortcutManagement.IShortcutManager.DeleteProfile.html) makes
it not available anymore.  
  
It also maintains a reference to the _active_ profile
([activeProfileId](ShortcutManagement.IShortcutManager-activeProfileId.html))
which determines the active bindings based on the shortcut overrides of the
active profile.
[RebindShortcut](ShortcutManagement.IShortcutManager.RebindShortcut.html) and
[ClearShortcutOverride](ShortcutManagement.IShortcutManager.ClearShortcutOverride.html)
requires the active profile to not be _read-only_ (i.e.
[IsProfileReadOnly](ShortcutManagement.IShortcutManager.IsProfileReadOnly.html)
returns `false` for [activeProfileId](ShortcutManagement.IShortcutManager-
activeProfileId.html)) since these two methods modify the active profile.  
  
Finally, it maintains a list of available shortcuts which can be retrieved
with
[GetAvailableShortcuts](ShortcutManagement.IShortcutManager.GetAvailableShortcuts.html).
All methods that take a shortcut ID require that the shortcut is avaliable.

### Properties

[activeProfileId](ShortcutManagement.IShortcutManager-activeProfileId.html)|
Gets or sets the ID of the currently active profile.  
---|---  
  
### Public Methods

[ClearShortcutOverride](ShortcutManagement.IShortcutManager.ClearShortcutOverride.html)|
Clears the binding for shortcut with given shortcut ID from the active
profile.  
---|---  
[CreateProfile](ShortcutManagement.IShortcutManager.CreateProfile.html)|
Creates a new profile with the given profile ID.  
[DeleteProfile](ShortcutManagement.IShortcutManager.DeleteProfile.html)|
Deletes profile with the given profile ID.  
[GetAvailableProfileIds](ShortcutManagement.IShortcutManager.GetAvailableProfileIds.html)|
Returns an enumeration of all of avaliable profile IDs.  
[GetAvailableShortcutIds](ShortcutManagement.IShortcutManager.GetAvailableShortcutIds.html)|
Returns an enumeration of all available shortcut IDs.  
[GetShortcutBinding](ShortcutManagement.IShortcutManager.GetShortcutBinding.html)|
Returns the active binding for the given shortcut ID.  
[IsProfileIdValid](ShortcutManagement.IShortcutManager.IsProfileIdValid.html)|
Checks that the profile ID is valid.  
[IsProfileReadOnly](ShortcutManagement.IShortcutManager.IsProfileReadOnly.html)|
Is the profile for the given profile ID read-only?  
[IsShortcutOverridden](ShortcutManagement.IShortcutManager.IsShortcutOverridden.html)|
Does the active profile override the binding for the given shortcut ID?  
[RebindShortcut](ShortcutManagement.IShortcutManager.RebindShortcut.html)|
Rebinds the shortcut for the given shortcut ID to the given binding in the
active profile.  
[RenameProfile](ShortcutManagement.IShortcutManager.RenameProfile.html)|
Renames the ID of a profile.  
  
### Events

[activeProfileChanged](ShortcutManagement.IShortcutManager-
activeProfileChanged.html)| Raised when the ID of the active profile is
changed.  
---|---  
[shortcutBindingChanged](ShortcutManagement.IShortcutManager-
shortcutBindingChanged.html)| Raised when shortcut overrides are changed on
the active profile.  
  
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

