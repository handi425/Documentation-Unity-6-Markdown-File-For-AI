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

# AccessibilityNode

class in UnityEngine.Accessibility

/

Implemented
in:[UnityEngine.AccessibilityModule](UnityEngine.AccessibilityModule.html)

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

An instance of a node in the
[AccessibilityHierarchy](Accessibility.AccessibilityHierarchy.html),
representing an element in the UI that the screen reader can read, focus, and
execute actions on.

### Properties

[allowsDirectInteraction](Accessibility.AccessibilityNode-
allowsDirectInteraction.html)|  Whether this node allows direct touch
interaction for users.  
---|---  
[children](Accessibility.AccessibilityNode-children.html)|  The children nodes
of the node.  
[frame](Accessibility.AccessibilityNode-frame.html)|  The Rect represents the
position in screen coordinates of the node in the UI. This can be set directly
but it is recommended that frameGetter is set instead, so that the value can
be recalculated when necessary.  
[frameGetter](Accessibility.AccessibilityNode-frameGetter.html)|  Optional
delegate that can be set to calculate the frame for the node instead of
setting a flat value. If the frame of the node may change over time, this
delegate should be set instead of giving a one time value for the frame.  
[hint](Accessibility.AccessibilityNode-hint.html)|  Provides additional
information about the accessibility node. For example, the result of
performing an action on the node.  
[id](Accessibility.AccessibilityNode-id.html)|  The ID of this node.  
[isActive](Accessibility.AccessibilityNode-isActive.html)|  Whether this node
is active in the hierarchy. The default value is true.  
[isFocused](Accessibility.AccessibilityNode-isFocused.html)|  Whether the node
is focused by the screen reader.  
[label](Accessibility.AccessibilityNode-label.html)|  A string value that
succinctly describes this node. The label is the first thing read by the
screen reader when a node is focused.  
[parent](Accessibility.AccessibilityNode-parent.html)|  The parent of the
node. If the node is at the root level, the parent value is null.  
[role](Accessibility.AccessibilityNode-role.html)|  The role for the node.  
[state](Accessibility.AccessibilityNode-state.html)|  The state for the node.  
[value](Accessibility.AccessibilityNode-value.html)|  The value of this node.  
  
### Public Methods

[GetHashCode](Accessibility.AccessibilityNode.GetHashCode.html)|  A hash used
for comparisons.  
---|---  
[ToString](Accessibility.AccessibilityNode.ToString.html)|  Provides a
debugging string.  
  
### Events

[decremented](Accessibility.AccessibilityNode-decremented.html)|  Called when
the user of the screen reader decrements the content of the node.  
---|---  
[dismissed](Accessibility.AccessibilityNode-dismissed.html)|  Called when the
user of the screen reader dismisses this node.  
[focusChanged](Accessibility.AccessibilityNode-focusChanged.html)|  Called
when the node gains or loses screen reader focus.  
[incremented](Accessibility.AccessibilityNode-incremented.html)|  Called when
the user of the screen reader increments the content of the node.  
[selected](Accessibility.AccessibilityNode-selected.html)|  Called when the
user of the screen reader selects this node.  
  
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

