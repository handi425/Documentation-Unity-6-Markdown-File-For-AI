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

#  [PresetSelector](Presets.PresetSelector.html).ShowSelector

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

public static void ShowSelector(Object[] targets,
[Presets.Preset](Presets.Preset.html) currentSelection, bool
createNewAllowed);

## Declaration

public static void ShowSelector(Object[] targets,
[Presets.Preset](Presets.Preset.html) currentSelection, bool createNewAllowed,
Action<Preset> onSelectionChanged, Action<Preset,bool> onSelectionClosed);

### Parameters

targets | The list of objects to which the selected Preset is applied.  
---|---  
currentSelection | The selected Preset when the window is opened. Set to 'null' for no selection.  
createNewAllowed | Whether to show the 'Create New Preset...' button. Set to true to show the button. Set to false to hide this button.  
onSelectionChanged | Callback invoked when the selected Preset is changed. Provides the selected preset as argument.  
onSelectionClosed | Callback invoked when the PresetSelector window is closed. Provides as arguments the selected preset and whether or not the selction was cancelled.  
  
### Description

Opens a modal window to select a [Preset](Presets.Preset.html).

* * *

## Declaration

public static [Search.ISearchView](Search.ISearchView.html)
ShowSelector([Presets.PresetType](Presets.PresetType.html) presetType,
[Presets.Preset](Presets.Preset.html) currentSelection,
[SerializedProperty](SerializedProperty.html) presetProperty, bool
createNewAllowed);

### Parameters

presetType | Filters the list of Presets based on a specific [PresetType](Presets.PresetType.html).  
---|---  
currentSelection | The selected Preset when the window is opened. Set to 'null' for no selection.  
presetProperty | The SerializedProperty behind an ObjectField used to select preset assets.  
createNewAllowed | Whether to show the 'Create New Preset...' button. Set to true to show the button. Set to false to hide this button.  
  
### Returns

**ISearchView** Returns the search view.

### Description

Opens a modal window to select a [Preset](Presets.Preset.html) from an object
field backed by a [SerializedProperty](SerializedProperty.html).

* * *

**Obsolete** The PresetSelectorReceiver is deprecated. Please use
ShowSelector(Object[], Preset, bool).

## Declaration

public static void ShowSelector([Object](Object.html) target,
[Presets.Preset](Presets.Preset.html) currentSelection, bool createNewAllowed,
PresetSelectorReceiver eventReceiver);

**Obsolete** The PresetSelectorReceiver is deprecated. Please use
ShowSelector(Object[], Preset, bool).

## Declaration

public static void ShowSelector([Presets.PresetType](Presets.PresetType.html)
presetType, [Presets.Preset](Presets.Preset.html) currentSelection, bool
createNewAllowed, PresetSelectorReceiver eventReceiver);

### Parameters

target | Object that identifies the type of Preset asset being selected. The modal window filters the selector view based on this object.  
---|---  
currentSelection | The selected Preset when the window is opened. Set to 'null' for no selection.  
createNewAllowed | Whether to show the 'Create New Preset...' button. Set to true to show the button. Set to false to hide this button.  
eventReceiver | The PresetSelectorReceiver instance that the PresetSelector uses to send events.  
presetType | Filters the list of Presets based on a specific PresetType. Use this param to set the PresetType when no target is specified.  
  
### Description

OBSOLETE. Opens a modal window to select a [Preset](Presets.Preset.html).

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

