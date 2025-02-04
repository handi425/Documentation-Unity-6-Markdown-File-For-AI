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

#  [ColorUtility](ColorUtility.html).TryParseHtmlString

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

public static bool TryParseHtmlString(string htmlString, out
[Color](Color.html) color);

### Parameters

htmlString | Case insensitive html string to be converted into a color.  
---|---  
color | The converted color.  
  
### Returns

**bool** True if the string was successfully converted else false.

### Description

Attempts to convert a html color string.

**Strings that begin with '#' will be parsed as hexadecimal in the following
way:**  
#RGB (becomes RRGGBB)  
#RRGGBB  
#RGBA (becomes RRGGBBAA)  
#RRGGBBAA  
  
When not specified alpha will default to FF.  
**Strings that do not begin with '#' will be parsed as literal colors, with
the following supported:**  
red, cyan, blue, darkblue, lightblue, purple, yellow, lime, fuchsia, white,
silver, grey, black, orange, brown, maroon, green, olive, navy, teal, aqua,
magenta..  
  
The following example creates a custom PropertyDrawer that allows the user to
input html colors. This property drawer can be shown in the inspector when a
color property has the attribute ColorHtmlProperty.  
  
![](../StaticFiles/ScriptRefImages/HexColorPropertyDrawer.png)  
_our custom property drawer._

    
    
    // This is not an editor script.
    using UnityEngine;  
      
    public class ColorHtmlPropertyAttribute : [PropertyAttribute](PropertyAttribute.html)
    {
    }
    
    
    
    // This is an editor script and should be placed in an '[Editor](Editor.html)' directory.
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    [[CustomPropertyDrawer](CustomPropertyDrawer.html)(typeof(ColorHtmlPropertyAttribute))]
    public class ColorHtmlPropertyDrawer : [PropertyDrawer](PropertyDrawer.html)
    {
        public override void OnGUI([Rect](Rect.html) position, [SerializedProperty](SerializedProperty.html) property, [GUIContent](GUIContent.html) label)
        {
            [Rect](Rect.html) htmlField = new [Rect](Rect.html)(position.x, position.y, position.width - 100, position.height);
            [Rect](Rect.html) colorField = new [Rect](Rect.html)(position.x + htmlField.width, position.y, position.width - htmlField.width, position.height);  
      
            string htmlValue = [EditorGUI.TextField](EditorGUI.TextField.html)(htmlField, label, "#" + [ColorUtility.ToHtmlStringRGBA](ColorUtility.ToHtmlStringRGBA.html)(property.colorValue));  
      
            [Color](Color.html) newCol;
            if ([ColorUtility.TryParseHtmlString](ColorUtility.TryParseHtmlString.html)(htmlValue, out newCol))
                property.colorValue = newCol;  
      
            property.colorValue = [EditorGUI.ColorField](EditorGUI.ColorField.html)(colorField, property.colorValue);
        }
    }
    
    
    
    // This shows how we would use the [PropertyDrawer](PropertyDrawer.html).
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        [ColorHtmlProperty]
        public [Color](Color.html) htmlColor = [Color.green](Color-green.html);  
      
        public [Color](Color.html) standardColor = [Color.green](Color-green.html);
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

