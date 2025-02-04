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

**Experimental** : this API is experimental and might be changed or removed in
the future.

#
[ITransitionAnimations](UIElements.Experimental.ITransitionAnimations.html).Start

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

public ValueAnimation<float> Start(float from, float to, int durationMs,
Action<VisualElement,float> onValueChanged);

### Parameters

from | Start value.  
---|---  
to | End value.  
durationMs | Duration of the transition in milliseconds.  
onValueChanged | Callback that applies the interpolated value.  
  
### Returns

**ValueAnimation <float>** The created animation object.

### Description

Starts a transition animation on this VisualElement.

* * *

## Declaration

public ValueAnimation<Rect> Start([Rect](Rect.html) from, [Rect](Rect.html)
to, int durationMs, Action<VisualElement,Rect> onValueChanged);

### Parameters

from | Start value.  
---|---  
to | End value.  
durationMs | Duration of the transition in milliseconds.  
onValueChanged | Callback that applies the interpolated value.  
  
### Returns

**ValueAnimation <Rect>** The created animation object.

### Description

Starts a transition animation on this VisualElement.

* * *

## Declaration

public ValueAnimation<Color> Start([Color](Color.html) from,
[Color](Color.html) to, int durationMs, Action<VisualElement,Color>
onValueChanged);

### Parameters

from | Start value.  
---|---  
to | End value.  
durationMs | Duration of the transition in milliseconds.  
onValueChanged | Callback that applies the interpolated value.  
  
### Returns

**ValueAnimation <Color>** The created animation object.

### Description

Starts a transition animation on this VisualElement.

* * *

## Declaration

public ValueAnimation<Vector3> Start([Vector3](Vector3.html) from,
[Vector3](Vector3.html) to, int durationMs, Action<VisualElement,Vector3>
onValueChanged);

### Parameters

from | Start value.  
---|---  
to | End value.  
durationMs | Duration of the transition in milliseconds.  
onValueChanged | Callback that applies the interpolated value.  
  
### Returns

**ValueAnimation <Vector3>** The created animation object.

### Description

Starts a transition animation on this VisualElement.

* * *

## Declaration

public ValueAnimation<Vector2> Start([Vector2](Vector2.html) from,
[Vector2](Vector2.html) to, int durationMs, Action<VisualElement,Vector2>
onValueChanged);

### Parameters

from | Start value.  
---|---  
to | End value.  
durationMs | Duration of the transition in milliseconds.  
onValueChanged | Callback that applies the interpolated value.  
  
### Returns

**ValueAnimation <Vector2>** The created animation object.

### Description

Starts a transition animation on this VisualElement.

* * *

## Declaration

public ValueAnimation<Quaternion> Start([Quaternion](Quaternion.html) from,
[Quaternion](Quaternion.html) to, int durationMs,
Action<VisualElement,Quaternion> onValueChanged);

### Parameters

from | Start value.  
---|---  
to | End value.  
durationMs | Duration of the transition in milliseconds.  
onValueChanged | Callback that applies the interpolated value.  
  
### Returns

**ValueAnimation <Quaternion>** The created animation object.

### Description

Starts a transition animation on this VisualElement.

* * *

## Declaration

public ValueAnimation<StyleValues>
Start([UIElements.Experimental.StyleValues](UIElements.Experimental.StyleValues.html)
from,
[UIElements.Experimental.StyleValues](UIElements.Experimental.StyleValues.html)
to, int durationMs);

### Parameters

from | Start value.  
---|---  
to | End value.  
durationMs | Duration of the transition in milliseconds.  
  
### Returns

**ValueAnimation <StyleValues>** The created animation object.

### Description

Starts a transition animation on this VisualElement.

* * *

## Declaration

public ValueAnimation<StyleValues>
Start([UIElements.Experimental.StyleValues](UIElements.Experimental.StyleValues.html)
to, int durationMs);

### Parameters

to | End value.  
---|---  
durationMs | Duration of the transition in milliseconds.  
  
### Returns

**ValueAnimation <StyleValues>** The created animation object.

### Description

Starts a transition animation on this VisualElement.

* * *

## Declaration

public ValueAnimation<float> Start(Func<VisualElement,float> fromValueGetter,
float to, int durationMs, Action<VisualElement,float> onValueChanged);

### Parameters

fromValueGetter | Callback that provides the initial value.  
---|---  
to | End value.  
durationMs | Duration of the transition in milliseconds.  
onValueChanged | Callback that applies the interpolated value.  
  
### Returns

**ValueAnimation <float>** The created animation object.

### Description

Starts a transition animation on this VisualElement.

* * *

## Declaration

public ValueAnimation<Rect> Start(Func<VisualElement,Rect> fromValueGetter,
[Rect](Rect.html) to, int durationMs, Action<VisualElement,Rect>
onValueChanged);

### Parameters

fromValueGetter | Callback that provides the initial value.  
---|---  
to | End value.  
durationMs | Duration of the transition in milliseconds.  
onValueChanged | Callback that applies the interpolated value.  
  
### Returns

**ValueAnimation <Rect>** The created animation object.

### Description

Starts a transition animation on this VisualElement.

* * *

## Declaration

public ValueAnimation<Color> Start(Func<VisualElement,Color> fromValueGetter,
[Color](Color.html) to, int durationMs, Action<VisualElement,Color>
onValueChanged);

### Parameters

fromValueGetter | Callback that provides the initial value.  
---|---  
to | End value.  
durationMs | Duration of the transition in milliseconds.  
onValueChanged | Callback that applies the interpolated value.  
  
### Returns

**ValueAnimation <Color>** The created animation object.

### Description

Starts a transition animation on this VisualElement.

* * *

## Declaration

public ValueAnimation<Vector3> Start(Func<VisualElement,Vector3>
fromValueGetter, [Vector3](Vector3.html) to, int durationMs,
Action<VisualElement,Vector3> onValueChanged);

### Parameters

fromValueGetter | Callback that provides the initial value.  
---|---  
to | End value.  
durationMs | Duration of the transition in milliseconds.  
onValueChanged | Callback that applies the interpolated value.  
  
### Returns

**ValueAnimation <Vector3>** The created animation object.

### Description

Starts a transition animation on this VisualElement.

* * *

## Declaration

public ValueAnimation<Vector2> Start(Func<VisualElement,Vector2>
fromValueGetter, [Vector2](Vector2.html) to, int durationMs,
Action<VisualElement,Vector2> onValueChanged);

### Parameters

fromValueGetter | Callback that provides the initial value.  
---|---  
to | End value.  
durationMs | Duration of the transition in milliseconds.  
onValueChanged | Callback that applies the interpolated value.  
  
### Returns

**ValueAnimation <Vector2>** The created animation object.

### Description

Starts a transition animation on this VisualElement.

* * *

## Declaration

public ValueAnimation<Quaternion> Start(Func<VisualElement,Quaternion>
fromValueGetter, [Quaternion](Quaternion.html) to, int durationMs,
Action<VisualElement,Quaternion> onValueChanged);

### Parameters

fromValueGetter | Callback that provides the initial value.  
---|---  
to | End value.  
durationMs | Duration of the transition in milliseconds.  
onValueChanged | Callback that applies the interpolated value.  
  
### Returns

**ValueAnimation <Quaternion>** The created animation object.

### Description

Starts a transition animation on this VisualElement.

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

