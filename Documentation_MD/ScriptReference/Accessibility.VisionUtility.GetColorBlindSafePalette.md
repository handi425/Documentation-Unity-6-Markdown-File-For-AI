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

#  [VisionUtility](Accessibility.VisionUtility.html).GetColorBlindSafePalette

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

public static int GetColorBlindSafePalette(Color[] palette, float
minimumLuminance, float maximumLuminance);

### Parameters

palette | An array of colors to populate with a palette.  
---|---  
minimumLuminance | Minimum allowable perceived luminance from 0 to 1. A value of 0.2 or greater is recommended for dark backgrounds.  
maximumLuminance | Maximum allowable perceived luminance from 0 to 1. A value of 0.8 or less is recommended for light backgrounds.  
  
### Returns

**int** The number of unambiguous colors in the palette.

### Description

Gets a palette of colors that should be distinguishable for normal vision,
deuteranopia, protanopia, and tritanopia.

![](../StaticFiles/ScriptRefImages/ColorBlindSafePaletteTable.png) _The set of
colors from which to draw, along with their perceived luminance values._  
  
Allocate the size of your palette before passing it to this method to specify
how many colors you need. The return value indicates how many unambiguous
colors exist in the palette. If this value is less than the size of the
palette, then the palette repeats colors in order.  
  
![](../StaticFiles/ScriptRefImages/ColorBlindSafePalette.png) _A window to
preview swatches that should be distinguishable for most vision conditions._  
  
Add the following script to Assets/Editor as ColorSwatchExample.cs and
navigate to the menu option Window -> Color Swatch Example.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using UnityEngine.Accessibility;  
      
    public class ColorSwatchExample : [EditorWindow](EditorWindow.html)
    {
        // size of swatch background textures to generate
        private const int k_SwatchTextureSize = 16;
        // the maximum number of swatches for this example
        private const int k_MaxPaletteSize = 10;  
      
        [[MenuItem](MenuItem.html)("Window/[Color](Color.html) Swatch Example")]
        private static void CreateWindow()
        {
            var window = GetWindow<ColorSwatchExample>();
            window.position = new [Rect](Rect.html)(0f, 0f, 400f, 80f);
        }  
      
        // the background textures to use for the swatches
        private [Texture2D](Texture2D.html)[] m_SwatchBackgrounds = new [Texture2D](Texture2D.html)[k_MaxPaletteSize];  
      
        // the desired number of swatches
        [[SerializeField](SerializeField.html)]
        private int m_PaletteSize = 8;
        // the range of desired luminance values
        [[SerializeField](SerializeField.html)]
        private [Vector2](Vector2.html) m_DesiredLuminance = new [Vector2](Vector2.html)(0.2f, 0.9f);
        // the colors obtained
        [[SerializeField](SerializeField.html)]
        private [Color](Color.html)[] m_Palette;
        // the number of unique colors in the palette before they repeat
        [[SerializeField](SerializeField.html)]
        private int m_NumUniqueColors;  
      
        // create swatch background textures when window first opens
        protected virtual void OnEnable()
        {
            titleContent = new [GUIContent](GUIContent.html)("[Color](Color.html) Swatches");  
      
            // create background swatches with different patterns for repeated colors
            m_SwatchBackgrounds[0] = CreateSwatchBackground(k_SwatchTextureSize, 0, 0);
            m_SwatchBackgrounds[1] = CreateSwatchBackground(k_SwatchTextureSize, 1, 4);
            m_SwatchBackgrounds[2] = CreateSwatchBackground(k_SwatchTextureSize, 1, 3);
            m_SwatchBackgrounds[3] = CreateSwatchBackground(k_SwatchTextureSize, 6, 1);
            m_SwatchBackgrounds[4] = CreateSwatchBackground(k_SwatchTextureSize, 4, 3);
            m_SwatchBackgrounds[5] = CreateSwatchBackground(k_SwatchTextureSize, 6, 6);
            m_SwatchBackgrounds[6] = CreateSwatchBackground(k_SwatchTextureSize, 4, 2);
            m_SwatchBackgrounds[7] = CreateSwatchBackground(k_SwatchTextureSize, 6, 4);
            m_SwatchBackgrounds[8] = CreateSwatchBackground(k_SwatchTextureSize, 2, 5);
            m_SwatchBackgrounds[9] = CreateSwatchBackground(k_SwatchTextureSize, 1, 2);  
      
            UpdatePalette();
        }  
      
        // clean up textures when window is closed
        protected virtual void OnDisable()
        {
            for (int i = 0, count = m_SwatchBackgrounds.Length; i < count; ++i)
                DestroyImmediate(m_SwatchBackgrounds[i]);
        }  
      
        protected virtual void OnGUI()
        {
            // input desired number of colors and luminance values
            [EditorGUI.BeginChangeCheck](EditorGUI.BeginChangeCheck.html)();  
      
            m_PaletteSize = [EditorGUILayout.IntSlider](EditorGUILayout.IntSlider.html)("Palette Size", m_PaletteSize, 0, k_MaxPaletteSize);  
      
            float min = m_DesiredLuminance.x;
            float max = m_DesiredLuminance.y;
            [EditorGUILayout.MinMaxSlider](EditorGUILayout.MinMaxSlider.html)("Luminance Range", ref min, ref max, 0f, 1f);
            m_DesiredLuminance = new [Vector2](Vector2.html)(min, max);  
      
            if ([EditorGUI.EndChangeCheck](EditorGUI.EndChangeCheck.html)())
            {
                UpdatePalette();
            }  
      
            // display warning message if parameters are out of range
            if (m_NumUniqueColors == 0)
            {
                string warningMessage = "Unable to generate any unique colors with the specified luminance requirements.";
                [EditorGUILayout.HelpBox](EditorGUILayout.HelpBox.html)(warningMessage, [MessageType.Warning](MessageType.Warning.html));
            }
            // otherwise display swatches in a row
            else
            {
                using (new [GUILayout.HorizontalScope](GUILayout.HorizontalScope.html)())
                {
                    [GUILayout.FlexibleSpace](GUILayout.FlexibleSpace.html)();
                    [Color](Color.html) oldColor = [GUI.color](GUI-color.html);  
      
                    int swatchBackgroundIndex = 0;
                    for (int i = 0; i < m_PaletteSize; ++i)
                    {
                        // change swatch background pattern when reaching a repeated color
                        if (i > 0 && i % m_NumUniqueColors == 0)
                            ++swatchBackgroundIndex;  
      
                        [Rect](Rect.html) rect = [GUILayoutUtility.GetRect](GUILayoutUtility.GetRect.html)(k_SwatchTextureSize * 2, k_SwatchTextureSize * 2);
                        rect.width = k_SwatchTextureSize * 2;  
      
                        [GUI.color](GUI-color.html) = m_Palette[i];
                        [GUI.DrawTexture](GUI.DrawTexture.html)(rect, m_SwatchBackgrounds[swatchBackgroundIndex], [ScaleMode.ScaleToFit](ScaleMode.ScaleToFit.html), true);
                    }  
      
                    [GUI.color](GUI-color.html) = oldColor;
                    [GUILayout.FlexibleSpace](GUILayout.FlexibleSpace.html)();
                }
            }
        }  
      
        // create a white texture with some pixels discarded to make a pattern
        private [Texture2D](Texture2D.html) CreateSwatchBackground(int size, int discardPixelCount, int discardPixelStep)
        {
            var swatchBackground = new [Texture2D](Texture2D.html)(size, size);
            swatchBackground.hideFlags = [HideFlags.HideAndDontSave](HideFlags.HideAndDontSave.html);
            swatchBackground.filterMode = [FilterMode.Point](FilterMode.Point.html);  
      
            var pixels = swatchBackground.GetPixels32();
            int counter = 0;
            bool discard = false;
            for (int i = 0, count = pixels.Length; i < count; ++i)
            {
                pixels[i] = new [Color32](Color32.html)(255, 255, 255, (byte)(discard ? 0 : 255));
                ++counter;
                if (discard && counter == discardPixelCount)
                {
                    discard = false;
                    counter = 0;
                }
                else if (!discard && counter == discardPixelStep)
                {
                    discard = true;
                    counter = 0;
                }
            }
            swatchBackground.SetPixels32(pixels);  
      
            swatchBackground.Apply();
            return swatchBackground;
        }  
      
        // request new palette
        private void UpdatePalette()
        {
            m_Palette = new [Color](Color.html)[m_PaletteSize];
            m_NumUniqueColors =
                [VisionUtility.GetColorBlindSafePalette](Accessibility.VisionUtility.GetColorBlindSafePalette.html)(m_Palette, m_DesiredLuminance.x, m_DesiredLuminance.y);
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

