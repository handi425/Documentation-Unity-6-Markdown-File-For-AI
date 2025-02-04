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

# GUISkin

class in UnityEngine

/

Inherits from:[ScriptableObject](ScriptableObject.html)

/

Implemented in:[UnityEngine.IMGUIModule](UnityEngine.IMGUIModule.html)

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

[Switch to Manual](../Manual/class-GUISkin.html "Go to GUISkin Component in
the Manual")

### Description

Defines how GUI looks and behaves.

GUISkin contains GUI settings and a collection of [GUIStyle](GUIStyle.html)
objects that together specify GUI skin.  
  
Active GUI skin is get and set through [GUI.skin](GUI-skin.html).

### Properties

[box](GUISkin-box.html)| Style used by default for GUI.Box controls.  
---|---  
[button](GUISkin-button.html)| Style used by default for GUI.Button controls.  
[customStyles](GUISkin-customStyles.html)| Array of GUI styles for specific
needs.  
[font](GUISkin-font.html)| The default font to use for all styles.  
[horizontalScrollbar](GUISkin-horizontalScrollbar.html)| Style used by default
for the background part of GUI.HorizontalScrollbar controls.  
[horizontalScrollbarLeftButton](GUISkin-horizontalScrollbarLeftButton.html)|
Style used by default for the left button on GUI.HorizontalScrollbar controls.  
[horizontalScrollbarRightButton](GUISkin-horizontalScrollbarRightButton.html)|
Style used by default for the right button on GUI.HorizontalScrollbar
controls.  
[horizontalScrollbarThumb](GUISkin-horizontalScrollbarThumb.html)| Style used
by default for the thumb that is dragged in GUI.HorizontalScrollbar controls.  
[horizontalSlider](GUISkin-horizontalSlider.html)| Style used by default for
the background part of GUI.HorizontalSlider controls.  
[horizontalSliderThumb](GUISkin-horizontalSliderThumb.html)| Style used by
default for the thumb that is dragged in GUI.HorizontalSlider controls.  
[label](GUISkin-label.html)| Style used by default for GUI.Label controls.  
[scrollView](GUISkin-scrollView.html)| Style used by default for the
background of ScrollView controls (see GUI.BeginScrollView).  
[settings](GUISkin-settings.html)| Generic settings for how controls should
behave with this skin.  
[textArea](GUISkin-textArea.html)| Style used by default for GUI.TextArea
controls.  
[textField](GUISkin-textField.html)| Style used by default for GUI.TextField
controls.  
[toggle](GUISkin-toggle.html)| Style used by default for GUI.Toggle controls.  
[verticalScrollbar](GUISkin-verticalScrollbar.html)| Style used by default for
the background part of GUI.VerticalScrollbar controls.  
[verticalScrollbarDownButton](GUISkin-verticalScrollbarDownButton.html)| Style
used by default for the down button on GUI.VerticalScrollbar controls.  
[verticalScrollbarThumb](GUISkin-verticalScrollbarThumb.html)| Style used by
default for the thumb that is dragged in GUI.VerticalScrollbar controls.  
[verticalScrollbarUpButton](GUISkin-verticalScrollbarUpButton.html)| Style
used by default for the up button on GUI.VerticalScrollbar controls.  
[verticalSlider](GUISkin-verticalSlider.html)| Style used by default for the
background part of GUI.VerticalSlider controls.  
[verticalSliderThumb](GUISkin-verticalSliderThumb.html)| Style used by default
for the thumb that is dragged in GUI.VerticalSlider controls.  
[window](GUISkin-window.html)| Style used by default for Window controls
(Additional resources: GUI.Window).  
  
### Public Methods

[FindStyle](GUISkin.FindStyle.html)| Try to search for a GUIStyle. This
functions returns NULL and does not give an error.  
---|---  
[GetStyle](GUISkin.GetStyle.html)| Get a named GUIStyle.  
  
### Inherited Members

### Properties

[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
---|---  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
---|---  
[ToString](Object.ToString.html)| Returns the name of the object.  
  
### Static Methods

[Destroy](Object.Destroy.html)| Removes a GameObject, component or asset.  
---|---  
[DestroyImmediate](Object.DestroyImmediate.html)| Destroys the object obj
immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](Object.DontDestroyOnLoad.html)| Do not destroy the target
Object when loading a new Scene.  
[FindAnyObjectByType](Object.FindAnyObjectByType.html)| Retrieves any active
loaded object of Type type.  
[FindFirstObjectByType](Object.FindFirstObjectByType.html)| Retrieves the
first active loaded object of Type type.  
[FindObjectsByType](Object.FindObjectsByType.html)| Retrieves a list of all
loaded objects of Type type.  
[Instantiate](Object.Instantiate.html)| Clones the object original and returns
the clone.  
[InstantiateAsync](Object.InstantiateAsync.html)| Captures a snapshot of the
original object (that must be related to some GameObject) and returns the
AsyncInstantiateOperation.  
[CreateInstance](ScriptableObject.CreateInstance.html)| Creates an instance of
a scriptable object.  
  
### Operators

[bool](Object-operator_Object.html)| Does the object exist?  
---|---  
[operator !=](Object-operator_ne.html)| Compares if two objects refer to a
different object.  
[operator ==](Object-operator_eq.html)| Compares two object references to see
if they refer to the same object.  
  
### Messages

[Awake](ScriptableObject.Awake.html)| Called when an instance of
ScriptableObject is created.  
---|---  
[OnDestroy](ScriptableObject.OnDestroy.html)| This function is called when the
scriptable object will be destroyed.  
[OnDisable](ScriptableObject.OnDisable.html)| This function is called when the
scriptable object goes out of scope.  
[OnEnable](ScriptableObject.OnEnable.html)| This function is called when the
object is loaded.  
[OnValidate](ScriptableObject.OnValidate.html)| Editor-only function that
Unity calls when the script is loaded or a value changes in the Inspector.  
[Reset](ScriptableObject.Reset.html)| Reset to default values.  
  
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

