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

# DecoratorDrawer

class in UnityEditor

/

Inherits from:[GUIDrawer](GUIDrawer.html)

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

Base class to derive custom decorator drawers from.

A DecoratorDrawer is similar to a [PropertyDrawer](PropertyDrawer.html),
except that it doesn't draw a property but rather draws decorative elements
based purely on the data it gets from its corresponding
[PropertyAttribute](PropertyAttribute.html).  
  
Unity uses builtin DecoratorDrawers for the
[SpaceAttribute](SpaceAttribute.html) and
[HeaderAttribute](HeaderAttribute.html). You can also create your own
DecoratorDrawers with matching PropertyAttributes.  
  
Although a DecoratorDrawer conceptually is not meant to be associated with a
specific field, its attribute still needs to be placed above a field in the
script. However, unlike PropertyDrawer attributes, there can be multiple
DecoratorDrawers attributes above the same field. Also unlike PropertyDrawers,
if a DecoratorDrawer attribute is placed above a field that is a List or an
array, the decorator will only show up once before the array; not for every
array element.  
  
**Note** : If you need your decorator drawer to perform cleanup tasks, such as
detaching itself from editor events, you can implement the
[IDisposable](https://learn.microsoft.com/en-us/dotnet/api/system.idisposable)
interface. This interface allows you to define a method that will be invoked
when the Editor is being destroyed, giving you the opportunity to handle any
necessary cleanup operations.  
  
The example below comes in two scripts.  
  
The first script defines the an example attribute called "ColorSpacer", and
then defines a DecoratorDrawer which determines how it should be drawn in the
inspector.  
  
The second script is an example MonoBehaviour which uses the ColorSpacer
attribute to visually separate two groups of public properties in the
inspector.

    
    
    // Name this script "ColorSpacerExample"  
      
    using UnityEngine;
    using System.Collections;
    using [UnityEditor](UnityEditor.html);  
      
    // This class defines the ColorSpacer attribute, so that
    // it can be used in your regular [MonoBehaviour](MonoBehaviour.html) scripts:  
      
    public class ColorSpacer : [PropertyAttribute](PropertyAttribute.html)
    {
        public float spaceHeight;
        public float lineHeight;
        public float lineWidth;
        public [Color](Color.html) lineColor = [Color.red](Color-red.html);  
      
        public ColorSpacer(float spaceHeight, float lineHeight, float lineWidth, float r, float g, float b)
        {
            this.spaceHeight = spaceHeight;
            this.lineHeight = lineHeight;
            this.lineWidth = lineWidth;  
      
            // unfortunately we can't pass a color through as a [Color](Color.html) object
            // so we pass as 3 floats and make the object here
            this.lineColor = new [Color](Color.html)(r, g, b);
        }
    }  
      
    
    // This defines how the ColorSpacer should be drawn
    // in the inspector, when inspecting a [GameObject](GameObject.html) with
    // a [MonoBehaviour](MonoBehaviour.html) which uses the ColorSpacer attribute  
      
    [[CustomPropertyDrawer](CustomPropertyDrawer.html)(typeof(ColorSpacer))]
    public class ColorSpacerDrawer : [DecoratorDrawer](DecoratorDrawer.html)
    {
        ColorSpacer colorSpacer
        {
            get { return ((ColorSpacer)attribute); }
        }  
      
        public override float GetHeight()
        {
            return base.GetHeight() + colorSpacer.spaceHeight;
        }  
      
        public override void OnGUI([Rect](Rect.html) position)
        {
            // calculate the rect values for where to draw the line in the inspector
            float lineX = (position.x + (position.width / 2)) - colorSpacer.lineWidth / 2;
            float lineY = position.y + (colorSpacer.spaceHeight / 2);
            float lineWidth = colorSpacer.lineWidth;
            float lineHeight = colorSpacer.lineHeight;  
      
            // Draw the line in the calculated place in the inspector
            [EditorGUI.DrawRect](EditorGUI.DrawRect.html)(new [Rect](Rect.html)(lineX, lineY, lineWidth, lineHeight), colorSpacer.lineColor);
        }
    }
    

And this second script is the one which makes use of the ColorSpacer attribute
defined above:

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ShowDecoratorDrawerExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public int a = 1;
        public int b = 2;
        public int c = 3;  
      
        // this shows our custom Decorator Drawer between the groups of properties
        [ColorSpacer(30, 3, 100, 1, 0, 0)]  
      
        public string d = "d";
        public string e = "e";
        public string f = "f";
    }
    

### Properties

[attribute](DecoratorDrawer-attribute.html)| The PropertyAttribute for the
decorator. (Read Only)  
---|---  
  
### Public Methods

[CreatePropertyGUI](DecoratorDrawer.CreatePropertyGUI.html)| Override this
method to make your own GUI for the property based on UIElements.  
---|---  
[GetHeight](DecoratorDrawer.GetHeight.html)| Override this method to specify
how tall the GUI for this decorator is in pixels.  
[OnGUI](DecoratorDrawer.OnGUI.html)| Override this method to make your own GUI
for the decorator. See DecoratorDrawer for an example of how to use this.  
  
### Inherited Members

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

